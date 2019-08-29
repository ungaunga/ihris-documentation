Help:Wikitext examples
======================

(From http://meta.wikimedia.org/wiki/Help:Wikitext_examples)

:''For basic information see [[Help:Editing]].''

Basic text formatting
^^^^^^^^^^^^^^^^^^^^^
You can format the page using Wikitext special characters.

{|width="80%"  border="1" cellpadding="2" cellspacing="0"
|-
!What it looks like
!What you type
|-
|
You can *italicize text*  by putting 2 
apostrophes on each side. 

3 apostrophes will **embolden the text** . 

5 apostrophes will **embolden**  and *italicize*  
 **the text** .

(Using 4 apostrophes doesn't do anything special -- <br>the last pair are just '''' left over ones'''' that are included as part of the text.)
|<pre>
You can *italicize text*  by putting 2 
apostrophes on each side. 

3 apostrophes will **embolden the text** . 

5 apostrophes will **embolden**  and *italicize* 
 **the text** .

(Using 4 apostrophes doesn't do anything
special -- <br /> the last pair are just ''''left
over ones'''' that are included as part
of the text.)
</pre>
|-
|
A single newline
generally has no effect on the layout.
These can be used to separate
sentences within a paragraph.
Some editors find that this aids editing
and improves the *diff*  function
(used internally to compare
different versions of a page).

But an empty line
starts a new paragraph.

When used in a list, a newline *does*  affect the layout ([[#lists|see below]]).
|<pre>
A single newline
generally has no effect on the layout.
These can be used to separate
sentences within a paragraph.
Some editors find that this aids editing
and improves the *diff*  function
(used internally to compare
different versions of a page).

But an empty line
starts a new paragraph.

When used in a list, a newline *does* 
affect the layout ([[#lists|see below]]).
</pre>
|-
|
You can break lines<br/>
without a new paragraph.<br/>
Please use this sparingly.

Please do not start a link or *italics*  or **bold**  text on one line and end on the next.
|<pre>
You can break lines<br/>
without a new paragraph.<br/>
Please use this sparingly.

Please do not start a link or
 *italics*  or **bold**  text on one line
and end on the next.
</pre>
|-
|
You should "sign" your comments on talk pages: <br/>
- Three tildes gives your signature: [[User:Example|Example]] <br/>
- Four tildes give your signature plus date/time: [[User:Example|Example]] 07:46, 27 November 2005 (UTC) <br/>
- Five tildes gives the date/time alone: 07:46, 27 November 2005 (UTC) <br/>
|<pre>
You should "sign" your comments 
on talk pages:
- Three tildes gives your
signature: ~~~
- Four tildes give your 
signature plus date/time: ~~~~
- Five tildes gives the 
date/time alone: ~~~~~
</pre>
|}


HTML tags
^^^^^^^^^
{{main|Help:HTML in wikitext}}
You can use some HTML tags, too. However, you should avoid HTML in favor of Wiki markup whenever possible.


{| border="1" cellpadding="1"
!width="1000"|What it looks like
!width="500"|What you type
|-
|
Put text in a <tt>typewriter
font</tt>. The same font is 
generally used for <code>
computer code</code>.
|<pre>
Put text in a <tt>typewriter
font</tt>. The same font is 
generally used for <code>
computer code</code>.
</pre>
|-
|
<strike>Strike out</strike>
or <u>underline</u> text,
or write it <span style=
"font-variant:small-caps">
in small caps</span>.
|<pre>
<strike>Strike out</strike>
or <u>underline</u> text,
or write it <span style=
"font-variant:small-caps">
in small caps</span>.
</pre>
|-
|
Superscripts and subscripts:
X<sup>2</sup>, H<sub>2</sub>O
|<pre>
Superscripts and subscripts:
X<sup>2</sup>, H<sub>2</sub>O
</pre>
|-
|
<center>Centered text</center>


* Please note the American spelling of "center".
|<pre>
<center>Centered text</center>


* Please note the American spelling of "center".
</pre>
|-
|
<blockquote>
The **blockquote**  command *formats*  block 
quotations, typically by surrounding them 
with whitespace and a slightly different font.
</blockquote>
|<pre>
<blockquote>
The **blockquote**  command formats block 
quotations, typically by surrounding them 
with whitespace and a slightly different font.
</blockquote>
</pre>
|-
|
Invisible comments to editors (&lt;!-- --&gt;) 
appear only while editing the page.
<!-- Note to editors: blah blah blah. -->



* If you wish to make comments to the public, you should usually use the [[talk page]].
|<pre>
Invisible comments to editors (<!-- -->)
appear only while editing the page.
<!-- Note to editors: blah blah blah. -->
</pre>
|}


Organizing your writing
^^^^^^^^^^^^^^^^^^^^^^^
{{seealso|w:Picture tutorial#Forcing a break|l1=Wikipedia:Picture tutorial#Forcing a break (not just for pictures).}}
{| border="1" cellspacing="2" 
!width="1000"|What it looks like
!width="500"|What you type
|-
|
<div style="font-size:150%;border-bottom:1px solid #000000;">Section headings</div>

 *Headings*  organize your writing into 
sections. The Wiki software can automatically 
generate a [[Help:table of contents|table of contents]] from them.

<div style="font-size:132%;font-weight:bold;">Subsection</div>
Using more "equals" (=) signs creates a subsection.

<div style="font-size:116%;font-weight:bold;">A smaller subsection</div>

Don't skip levels, like from two to four equals signs.

Start with 2 equals signs not 1 because 1 creates H1 tags which should be reserved for page title.
|<pre>

Section headings
^^^^^^^^^^^^^^^^

 *Headings*  organize your writing into
sections. 
The *Wiki*  <u>ab</u> 


  * software can automatically
generate a [[table of contents]] from them.


Subsection
~~~~~~~~~~
Using more "equals" (=) signs creates a subsection.


A smaller subsection
--------------------

Don't skip levels,
like from two to four equals signs.

Start with 2 equals signs not 1
because 1 creates H1 tags
which should be reserved for page title.
</pre>
|- id="lists"
|


* *Unordered [[Help:List|list]]s*  are easy to do:
* * Start every line with a star.
* ** More stars indicate a deeper level.
* : Previous item continues.
* * A newline
* in a list
marks the end of the list.


* Of course you can start again.
|<pre>


* *Unordered lists*  are easy to do:
* * Start every line with a star.
* ** More stars indicate a deeper level.
* : Previous item continues.
* * A newline
* in a list
marks the end of the list.


* Of course you can start again.
</pre>
|-
|

* *Numbered lists*  are:

  * Very organized
  * Easy to follow
A newline marks the end of the list.

* New numbering starts with 1.

|<pre>

* *Numbered lists*  are:

  * Very organized
  * Easy to follow
A newline marks the end of the list.

* New numbering starts with 1.
</pre>
|-
|
Here's a *definition list* :
; Word : Definition of the word
; A longer phrase needing definition
: Phrase defined
; A word : Which has a definition
: Also a second definition
: And even a third

Begin with a semicolon. One item per line; 
a newline can appear before the colon, but 
using a space before the colon improves 
parsing.
|<pre>
Here's a *definition list* :
; Word : Definition of the word
; A longer phrase needing definition
: Phrase defined
; A word : Which has a definition
: Also a second one
: And even a third

Begin with a semicolon. One item per line; 
a newline can appear before the colon, but 
using a space before the colon improves 
parsing.
</pre>
|-
|


* You can even do mixed lists
* # and nest them
* # inside each other
* #* or break lines<br>in lists.
* #; definition lists
* #: can be
* #:; nested : too
|<pre>


* You can even do mixed lists
* # and nest them
* # inside each other
* #* or break lines<br>in lists.
* #; definition lists
* #: can be
* #:; nested : too
</pre>
|-
|
: A colon (:) indents a line or paragraph.
A newline starts a new paragraph. <br>
Should only be used on [[talk page]]s. <br>
For articles, you probably want the blockquote tag.
: We use 1 colon to indent once.
:: We use 2 colons to indent twice.
::: 3 colons to indent 3 times, and so on.
|<pre>
: A colon (:) indents a line or paragraph.
A newline starts a new paragraph.
Should only be used on talk pages.
For articles, you probably want the blockquote tag.
: We use 1 colon to indent once.
:: We use 2 colons to indent twice.
::: 3 colons to indent 3 times, and so on.
</pre>
|-
|
You can make [[w:horizontal dividing line|horizontal dividing line]]s (----)
to separate text.
----
But you should usually use sections instead,
so that they go in the table of contents.
|<pre>
You can make horizontal dividing lines (----)
to separate text.
----
But you should usually use sections instead,
so that they go in the table of contents.
</pre>
|-
|
You can add footnotes to sentences using the *ref*  tag -- this is especially good for citing a source.

:There are over six billion people in the world.<ref>CIA World Factbook, 2006.</ref>

References: <references/>

For details, see [[Wikipedia:Footnotes]] and [[Help:Footnotes]].
|

.. code-block::

    You can add footnotes to sentences using
    the *ref*  tag -- this is especially good
    for citing a source.
    
    :There are over six billion people in the
    world.<ref>CIA World Factbook, 2006.</ref>
    
    References: <references/>
    
    For details, see [[Wikipedia:Footnotes]] 
    and [[Help:Footnotes]].
    

|}


Links
^^^^^
{{main|Help:Link}}
You will often want to make clickable *links*  to other pages.

{|width="100%"  border="1" cellpadding="2" cellspacing="0"
|-
!What it looks like
!What you type
|-
|
Here's a link to a page named [[Official position]].
You can even say [[official position]]s
and the link will show up correctly.
|<pre>
Here's a link to a page named [[Official position]].
You can even say [[official position]]s
and the link will show up correctly.
</pre>
|-
|
You can put [[formatting]] around a link.
Example: *[[Wikipedia]]* .
|<pre>
You can put formatting around a link.
Example: *[[Wikipedia]]* .
</pre>
|-
|
The *first letter*  of articles is automatically
capitalized, so [[wikipedia]] goes to the same place
as [[Wikipedia]]. Capitalization matters after the
first letter.
|<pre>
The *first letter*  of articles is automatically
capitalized, so [[wikipedia]] goes to the same place
as [[Wikipedia]]. Capitalization matters after the
first letter.
</pre>
|-
|
[[Intentionally permanent red link]] is a page that doesn't exist
yet. You could create it by clicking on the link.
|<pre>
[[Intentionally permanent red link]] is a page that doesn't exist
yet. You could create it by clicking on the link.
</pre>
|-
|
You can link to a page section by its title:



* [[List of cities by country#Morocco]].

If multiple sections have the same title, add
a number. [[#Example section 3]] goes to the
third section named "Example section".
|<pre>
You can link to a page section by its title:



* [[List of cities by country#Morocco]].

If multiple sections have the same title, add
a number. [[#Example section 3]] goes to the
third section named "Example section".
</pre>
|-
|
You can make a link point to a different place
with a [[Help:Piped link|piped link]]. Put the link
target first, then the pipe character "|", then
the link text.

* [[Help:Link|About Links]]
* [[List of cities by country#Morocco|Cities in Morocco]]

Or you can use the "pipe trick" so that a title that
contains disambiguation text will appear with more concise
link text.

* [[Spinning (textiles)|Spinning]]
* [[Boston, Massachusetts|Boston]]
|<pre>
You can make a link point to a different place
with a [[Help:Piped link|piped link]]. Put the link
target first, then the pipe character "|", then
the link text.

* [[Help:Link|About Links]]
* [[List of cities by country#Morocco|Cities in Morocco]]

Or you can use the "pipe trick" so that a title that
contains disambiguation text will appear with more concise
link text.

* [[Spinning (textiles)|]]
* [[Boston, Massachusetts|]]
</pre>
|-
|
You can make an external link just by typing a URL:
http://www.nupedia.com

You can give it a title:asd
 `Nupedia <http://www.nupedia.com>`_ 

Or leave the title blank:
[http://www.nupedia.com]

External link can be used to link to a wiki page that cannot be linked to with <nowiki>[[page]]</nowiki>:
http://meta.wikimedia.org/w/index.php?title=Fotonotes&oldid=482030#Installation
|

.. code-block::

    You can make an external link just by typing a URL:
    http://www.nupedia.com
    
    You can give it a title:
     `Nupedia <http://www.nupedia.com>`_ 
    
    Or leave the title blank:
    [http://www.nupedia.com]
    
    External link can be used to link to a wiki page that
    cannot be linked to with <nowiki>[[page]]</nowiki>:
    http://meta.wikimedia.org/w/index.php?title=Fotonotes
    &oldid=482030#Installation
    

|-
|
Linking to an e-mail address works the same way:
mailto:someone@example.com or [mailto:someone@example.com someone]
|

.. code-block::

    Linking to an e-mail address works the same way:
    mailto:someone@example.com or [mailto:someone@example.com someone]
    

|-
|
You can [[Help:Redirect|redirect]] the user to another page.
|<pre>
#REDIRECT [[Official position]]
</pre>
|-
|
[[Help:Category|Category links]] do not show up in line
but instead at page bottom
 *and cause the page to be listed in the category.* 

Add an extra colon to *link*  to a category in line
without causing the page to be listed in the category:
|<pre>
[[Help:Category|Category links]] do not show up in line
but instead at page bottom
 *and cause the page to be listed in the category.* 

Add an extra colon to *link*  to a category in line
without causing the page to be listed in the category:
</pre>
|-
|
The Wiki reformats linked dates to match the reader's
date preferences. These three dates will show up the
same if you choose a format in your
[[Special:Preferences|Preferences]]:
* [[1969-07-20]]
* [[July 20]], [[1969]]
* [[20 July]] [[1969]]
|<pre>
The Wiki reformats linked dates to match the reader's
date preferences. These three dates will show up the
same if you choose a format in your
[[Special:Preferences|]]:
* [[1969-07-20]]
* [[July 20]], [[1969]]
* [[20 July]] [[1969]]
</pre>
|}


Just show what I typed
^^^^^^^^^^^^^^^^^^^^^^

A few different kinds of formatting will tell the Wiki to display things as you typed them.

{| border="1" cellpadding="2"
!width="1000"|What it looks like
!width="500"|What you type
|-
|
<nowiki>
The nowiki tag ignores 
[[Wiki]] *markup* .
It reformats text by 
removing
newlines    and multiple
 spaces.
It still interprets special
characters: &rarr;
</nowiki>
|<pre>
&lt;nowiki&gt;
The nowiki tag ignores 
[[Wiki]] *markup* .
It reformats text by 
removing
newlines    and multiple
 spaces.
It still interprets special
characters: &amp;rarr;
&lt;/nowiki&gt;
</pre>
|-
|

.. code-block::

    The pre tag ignores [[Wiki]]
     *markup* .
    It also doesn't     reformat
     text.
    It still interprets special
    characters: &rarr;
    

|<pre>
&lt;pre&gt;
The pre tag ignores [[Wiki]]
 *markup* .
It also doesn't     reformat
 text.
It still interprets special
characters: &amp;rarr;
&lt;/pre&gt;
</pre>
|-
|
[[Leading spaces]] are another way to preserve formatting.

 Putting a space at the
 beginning of each
 line stops the text   
 from being
 reformatted.  It still 
 interprets [[Wiki]]
 *markup*  and special
 characters: &rarr;
|<pre>
Leading spaces are another way
to preserve formatting.

 Putting a space at the
 beginning of each
 line stops the text
 from being
 reformatted.  It still 
 interprets [[Wiki]]
 *markup*  and special
 characters: &amp;rarr;
</pre>
|}


Source code
~~~~~~~~~~~
{{main|mw:Extension:SyntaxHighlight GeSHi}}
If the syntax highlighting extension is installed, you can display programming language [[w:source code|source code]] in a manner very similar to the HTML <code><nowiki><pre></nowiki></code> tag, except with the type of [[w:syntax highlighting|syntax highlighting]] commonly found in advanced text editing software.

Here's an example of how to display some [[w:C Sharp (programming language)|C#]] source code:


.. code-block::

    <nowiki>
    

.. code-block:: csharp

        // Hello World in Microsoft C# ("C-Sharp").
        
        using System;
        
        class HelloWorld
        {
            public static int Main(String[] args)
            {
                Console.WriteLine("Hello, World!");
                return 0;
            }
        }
        

    </nowiki>


Results in:



.. code-block:: csharp

    // Hello World in Microsoft C# ("C-Sharp").
    
    using System;
    
    class HelloWorld
    {
        public static int Main(String[] args)
        {
            Console.WriteLine("Hello, World!");
            return 0;
        }
    }
    



Images, tables, video, and sounds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<i>This is a very quick introduction. For more information, see:
* [[Help:Images and other uploaded files]], for how to upload files;
* [[w:en:Wikipedia:Extended image syntax]], for how to arrange images on the page;
* [[Help:Table]], for how to create a table.</i>

After uploading, just enter the filename, highlight it and press the "embedded image"-button of the edit_toolbar.

This will produce the syntax for uploading a file **<nowiki>
.. image:: images/filename.png
    :align: center

</nowiki>** 

{| border="1" cellpadding="2"
!width="1000"|What it looks like
!width="500"|What you type
|-
|
A picture, including alternate text:


.. image:: images/Wiki.png
    :align: center



You can put the image in a frame with a caption:

.. image:: images/Wiki.png
    :align: center


|<pre>
A picture, including alternate text:


.. image:: images/Wiki.png
    :align: center



You can put the image in a frame with a caption:

.. image:: images/Wiki.png
    :align: center


</pre>
|-
|
A link to Wikipedia's page for the image:
[[:Image:Wiki.png]]

Or a link directly to the image itself:
[[Media:Wiki.png]]
|<pre>
A link to Wikipedia's page for the image:
[[:Image:Wiki.png]]

Or a link directly to the image itself:
[[Media:Wiki.png]]
</pre>
|-
|Use **media:**  links to link 
directly to sounds or videos: 
[[media:Classical guitar scale.ogg|A sound file]]
|<pre>
Use **media:**  links to link
directly to sounds or videos:
[[media:Classical guitar scale.ogg|A sound file]]
</pre>
|-
|Provide a spoken rendition of some text in a template:
{{listen
 |title    = Flow my tears
 |filename = Flow my tears.ogg
 |filesize = 583KB
}}
|<pre>
Provide a spoken rendition of some text in a template:
{{listen
 |title    = Flow my tears
 |filename = Flow my tears.ogg
 |filesize = 583KB
}}
</pre>
|-
|
{| border="1" cellspacing="0" cellpadding="5" align="center"
! This 
! is 
|- 
| a 
| table 
|}
|<pre>
{| border="1" cellspacing="0" cellpadding="5" align="center"
! This
! is
|- 
| a
| table
|}
</pre>
|}


Galleries
~~~~~~~~~
{{main|w:Gallery tag}}

<!-- The above link is incorrect. Since I'm not that great at wiki, I'll leave it to you to fix. The correct link should be to http://en.wikipedia.org/wiki/Wikipedia:Gallery_tag -->

Images can also be grouped into galleries using the <code><nowiki><gallery></nowiki></code> tag, such as the following:

<gallery>
Image:Wiki.png
Image:Wiki.png|Captioned
Image:Wiki.png
Image:Wiki.png|[[Wikipedia|Links]] can be put in captions.
</gallery>


Mathematical formulas
^^^^^^^^^^^^^^^^^^^^^
{{main|Help:Displaying a formula}}
You can format mathematical formulas with [[w:TeX|TeX]] markup.

{| border="1" cellpadding="2"
!width="1000"|What it looks like
!width="500"|What you type
|-
|
<math>\sum_{n=0}^\infty \frac{x^n}{n!}</math>
|<pre><nowiki>
<math>\sum_{n=0}^\infty \frac{x^n}{n!}</math>
</nowiki></pre>
|}


Templates
^^^^^^^^^
{{main|Help:Template}}
Templates are segments of Wiki markup that are meant to be copied automatically ("transcluded") into a page.
You add them by putting the template's name in <nowiki>{{double braces}}</nowiki>. It is also possible to transclude other pages by using <nowiki>{{:colon and double braces}}</nowiki>.

Some templates take *parameters* , as well, which you separate with the pipe character.

{| border="1" cellpadding="2"
!width="1000"|What it looks like
!width="500"|What you type
|-
|
{{Transclusion demo}}
|<pre>
{{Transclusion demo}}
</pre>
|-
|
{{Help:Transclusion Demo}}
|<pre>
{{Help:Transclusion Demo}}
</pre>
|-
|

This template takes two parameters, and
creates underlined text with a hover box
for many modern browsers supporting CSS:

{{H:title|This is the hover text|
Hover your mouse over this text}}

Go to this page to see the H:title template
itself: {{tl|H:title}}

|<pre>
This template takes two parameters, and
creates underlined text with a hover box
for many modern browsers supporting CSS:

{{H:title|This is the hover text|
Hover your mouse over this text}}

Go to this page to see the H:title template
itself: {{tl|H:title}}
</pre>
|}

[[Category:Implementer Resources]]
{{h:f|enname=Wikitext examples}}
