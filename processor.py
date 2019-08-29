import re
import os
from decorators import (heading, code_pre_block_converter, source_block_converter,
                    list_block_converter)

from threading import Thread
from utils import download_image

class WikimediaRSTConventer():
    '''
    Class for converting Wikimedia based documents into restructured
    text format documents.

    You can instantiate the class with a valid wikimedia-based site URL
    or with a file path. The file path should be for content that is extracted
    from the wiki site in edit mode.
    '''
    def __init__(self, doc_path='', doc_url = ''):
        self.doc_path = doc_path
        self.doc_url = doc_url
        self.save_to = re.sub(r'(.*?)(docs-base)(.*?)', r'\1docs\3', doc_path)

    
    def process_document(self):
        '''
        Processes the entire document and writes a rST formatted document
        when it is done.
        '''
        with open(f"{self.save_to}", 'w') as conv:
            with open(self.doc_path) as data:
                data = data.readlines()
                # data = doc.read()
                prev_line = ''
                for line in data:
                    l = self.convert_h2(self.convert_h3(self.convert_h4(self.convert_h5(self.convert_h6(line)))))
                    l = self.convert_external_links(l)
                    l = self.convert_bold(l)
                    l = self.convert_bold_italics(l)
                    l = self.convert_italics(l)
                    l = self.convert_image_attachments(l)
                    if prev_line.startswith('*'):
                        self.convert_ul(l)
                    prev_line = line
                    conv.write(l)
        f = open(f'{self.save_to}')
        txt = f.read()
        f.close()
        f = open(f'{self.save_to}', 'w')
        txt = self.convert_code_pre_blocks(txt)
        txt = self.convert_source_blocks(txt)
        txt = self.convert_ol(txt)
        f.write(txt)

    def convert_titles(self, doc):
        '''
        Converts all titles in a document. It does this by calling functions for changing specific
        titles
        '''
        pass
    
    def convert_ol(self, doc):
        '''
        Converts all ordered lists
        (?ms)^#+(.*?)\n(?!#)
        '''
        regex = r"(?ms)^((?:#|\*)+.*?)\n(?!(?:#|\*))"
        return re.sub(regex, list_block_converter, doc, re.DOTALL)
        
    def convert_ul(self, text):
        '''
        Converts unordered lists.
        For wiki ul, a list starts with * followed immediately by text *abcabc
        nested lists keep on appending *
        for rst, nested lists start on a new line
        '''
        # single bullet
        level1 = r'^*\w+'
        level2 = r'^**\w'
        level3 = r'^***\w'

    def convert_italics(self, doc):
        regex = r'(^|\s)([\']{2})(?!\')(.*?)\2'
        return re.sub(regex, r' *\3* ', doc)
    
    def convert_bold(self, doc):
        '''
        Converts all bold text. 
        Markup for bold in wiki based pages is \'''
        Markup for rst is **
        '''
        regex = r'(^|\s)([\']{3})(?!\')(.*?)\2'
        return re.sub(regex, r' **\3** ', doc)

    def convert_bold_italics(self, doc):
        regex = r'(^|\s)([\']{5})(?!\')(.*?)\2'
        return re.sub(regex, r' **\3** ', doc)

    def convert_code_pre_blocks(self, doc):
        '''
        Converts all <code> and <pre> blocks.
        (?ms) . matches new line chars '(?ms)^(<code>)\n*(.*?)(^<\/code>)'
        '''
        regex = r'(?ms)^(<code>|<pre>)\n*(.*?)(<\/code>|<\/pre>)'
        return re.sub(regex, code_pre_block_converter, doc, flags=re.DOTALL)

    def convert_source_blocks(self, doc):
        '''
        Converts all <source> blocks
        '''
        regex = r'(?ms)<source\s*(?:lang=\'|lang=\")?(\w+)?(?:\"|\')?>\n*(.*?)<\/source>'
        return re.sub(regex, source_block_converter, doc, re.DOTALL)

    def convert_tables(self, doc):
        pass

    def convert_image_attachments(self, doc):
        '''
        Converts wikimedia markup for images
        rst format  uses the directive
        .. image:: /path/to/image
            :alt: alt_text
            :height: height
            :width: width
            :align: "top", "middle", "bottom", "left", "center", or "right"
            :target: URI or reference name
        '''
        regex = r'\[\[(?:Image|File):(.*?\.(?:png|jpg|gif|jpeg)).*?\]\]'
        imgs = re.findall(regex, doc)
        if not os.path.exists(f'{os.path.dirname(self.save_to)}/images'):
            os.mkdir(f'{os.path.dirname(self.save_to)}/images')
        if imgs:
            download_image(file_name=imgs[0], save_to=f'{os.path.dirname(self.save_to)}/images')
        return re.sub(regex, r'\n.. image:: images/\1\n    :align: center\n\n', doc)

    def convert_internal_links(self, doc):
        '''
        Converts all internal links
        Wiki: [[Some Document Title]]
        reST: `Some Document Title <../../some-document-title>`_
        This assumes the URL was formatted like so and the file
        some-document-title resides two directories above this source
        '''
        pass
    
    def convert_external_links(self, doc):
        '''
        Converts external links
        Wiki: [URL hyperlink-text]
        reST: `hyperlink-text <URL>`_
        possible wiki external URL matcher: 
        '''
        regex = r"\[((?:http[s]{0,1}://)?(?:www\.)?(?:[\w\-]+\.)+[\w\-_.~!*'();:@&=+$,/?%#[\]]+)\s(.*?)]"
        return re.sub(regex, r' `\2 <\1>`_ ', doc)

    def convert_media_attachments(self, doc):
        pass

    @heading(marker='^')
    def convert_h2(self, doc):
        '''
        Converts all h2 titles in the document
        '''
        return re.sub(r'^(==)([^=].*?)(\1)', r'\2', doc)

    @heading(marker='~')
    def convert_h3(self, doc):
        '''
        Converts all h3 titles in the document
        '''
        return re.sub(r'^(===)([^=].*?)(\1)', r'\2', doc)
    
    @heading(marker='-')
    def convert_h4(self, doc):
        '''
        Converts all h4 titles in the document
        '''
        return re.sub(r'^(====)([^=].*?)(\1)', r'\2', doc)

    @heading(marker='#')
    def convert_h5(self, doc: str) -> str:
        '''
        Converts all h5 titles in the document
        '''
        return re.sub(r'^(=====)([^=].*?)(\1)', r'\2', doc)
    
    @heading(marker='*')
    def convert_h6(self, string: str) -> str:
        '''
        Converts all h6 titles in the document
        '''
        return re.sub(r'^(======)([^=].*?)(\1)', r'\2', string)
        

if __name__ == '__main__':
    def processor(dirpath):
        for entry in os.scandir(dirpath):
            if entry.is_file() and entry.name != 'index.rst':
                # print(f"processing {entry.path}")
                conv = WikimediaRSTConventer(doc_path=entry.path)
                print(f'saving to {conv.save_to}')
                conv.process_document()
            elif entry.is_dir():
                processor(entry.path)

    processor('docs-base')