import functools
import re
from pprint import pprint

def heading(*, marker=''):
    '''
    Add a new line with the same number of heading markers as the characters in the title
    Need to specify marker to one of the valid rst line markups
    '''
    def wrapper_heading(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            title = func(*args, **kwargs)
            class_obj, passed_title, = args
            title = title.strip()
            return f'\n{title}\n{marker*len(title)}\n' if passed_title.strip() != title else passed_title
        return wrapper
    return wrapper_heading

def code_pre_block(func):
    '''
    formats a code block according to rst format
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        block = func(*args, **kwargs)
        new_block = '\n.. code-block::\n\n'
        for line in block.split('\n'):
            new_block += f'    {line}\n'
        return new_block
    return wrapper

def source_block(func):
    '''
    formats code from <source lang="some_language"> blocks
    where the language is optional
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        lang, block = func(*args, **kwargs)
        new_block = f'\n\n.. code-block:: {lang or ""}\n\n'
        for line in block.split('\n'):
            new_block += f'    {line}\n'
        return new_block
    return wrapper

def list_block(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        items = func(*args, **kwargs)
        new_list = '\n'
        prev_indent = 0
        sub_list_started = False
        for line in items.split('\n'):
            num_markers = get_num_markers(line) # how many # there are
            indent_by = (num_markers - 1) * 2 # no indentation for first level
            def get_printable_part(string):
                '''
                trim out up to a colon or semi-colon after a # list marker
                '''
                return string[num_markers+1:].strip() if string[num_markers] in [':', ';', '*'] else string[num_markers:].strip()
            # if # is followed by ; or :, it is a continuation of the previous list item
            # this can just be indented
            if line[num_markers] == '*': # bullet list item
                if not sub_list_started:
                    new_list += f'\n{" " * num_markers*2}* {get_printable_part(line)}\n'
                    sub_list_started = True
                else:
                    new_list += f'{" " * num_markers*2}* {get_printable_part(line)}\n'
                continue
            sub_list_started = False
            if line[num_markers] in [':', ';']:
                line = f'{" " * num_markers*2}{get_printable_part(line)}'
            else:
                line = f'{" " * indent_by}* {get_printable_part(line)}'
            if indent_by != prev_indent: # starting a new level or going back to old level
                line = f'\n{line}' # new level starts a new line
                prev_indent = indent_by
            new_list += f'{line}\n'
        return new_list
    return wrapper

def get_num_markers(string):
    indent_by = 0
    for i in range(len(string)):
        if string[i] == '#':
            indent_by += 1
        else:
            break
    return indent_by

@list_block
def list_block_converter(match_group):
    return match_group.group(1)

@code_pre_block
def code_pre_block_converter(match_group):
    return match_group.group(2)

@source_block
def source_block_converter(match_group):
    '''
    formats a code block from <source lang="some_language">
    the language part is optional
    '''
    return (match_group.group(1), match_group.group(2))

if __name__ == '__main__':
    pass