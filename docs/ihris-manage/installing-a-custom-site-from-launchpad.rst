Installing a Custom Site from Launchpad
=======================================

In this tutorial, we will install a custom iHRIS Manage 4.0 site hosted on Launchpad. We will bazaar to download the code as well as discuss the basics on how to modify the code on Launchpad.  We are assuming that you are using an Ubuntu Linux machine.

Our first goal is to install the iHRIS Suite 4.0.  Then we will download the CSSC's iHRIS Manage Customizations.  Next we will create the database and finally we will install the site in our web-server.

==Launchpad First Steps==
First you should create an account on [https://launchpad.net/ Launchpad] if you not have already done so.  We will refer to this account as '''LAUNCHPAD_USER.'''

Since we will want to contribute to the code, we will need to create a [https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair ssh public key] on your Ubuntu machine to add to Launchpad:
 sudo apt-get install openssh-client
 ssh-keygen -t rsa
When prompted, press Enter to accept the default file name for your key. Next, enter then confirm a password to protect your SSH key.  

Your key pair is now stored in ~/.ssh/id_rsa.pub (public key) and ~/.ssh/id_rsa (private key). Now you need to upload the public portion of your SSH key to Launchpad. To do this, open in your web browser:
 https://www.launchpad.net/~'''LAUNCHPAD_USER'''
You will see a place that says ''SSH Keys'' with an exclamation point '''(!)''' in a yellow circle next to it.  Click on the '''(!)''' scroll down until you see ''Add an SSH Key'' and a text box.  We will paste our public key into this text box.  To do so type in a terminal:
 gedit ~/.ssh/id_rsa.pub
you can now copy the contents of gedit (the public key) into the text box in the web browser.  Now simply click on the button ''Import Public Key''

For every computer/account that you use you will need to repeat these steps to create and import a public key.

==Bazaar First Steps==
First we need to make sure the [http://bazaar-vcs.org/en/ Bazaaar] (bzr) version control software is installed:
  sudo apt-get install bzr bzrtools
You may wish to read the [http://doc.bazaar-vcs.org/latest/en/mini-tutorial/index.html five minute tutorial] at this point.  You should also let bzr know how you are:
  bzr whoami "'''Your Name <your@email.add.ress>'''"


==Join the iHRIS Team==
Launchpad uses "teams" to control who can modify code it stores under bazaar.

If you wish to make modifications to the CSSC Customizations, you should join the [http://www.launchpad.net/~ihris+cssc ihris+cssc] team.  

If you are working on a joint project, but not the CSSC's customizations, you should create a team in Launchpad and add yourself to it as well as the team ''intrahealth+informatics.''   For example, you could create the team ''ihris+tanzania.''



==Downloading iHRIS==
We will now download the iHRIS Suite from Launchpad using bzr (as opposed to the release tar.bz2 files) to get practice using bazaar.

Below, I will assume that there is only one user using the system, or at least only one user that should be modifying files in iHRIS.  This is probably not the "recommended" way of doing things though.

===Changing Permissions===
We want to make sure we can easily modify files under ''/var/lib/iHRIS'' without having to use sudo all the time.
 sudo mkdir -p /var/lib/iHRIS
 sudo chown -R `whoami`:`whoami`  /var/lib/iHRIS


===Release Code===
Now we want to get the iHRIS Suite 4.0 release code from launchpad.
 sudo mkdir -p /var/lib/iHRIS/lib/4.0
 sudo chown -R  `whoami`:`whoami` /var/lib/iHRIS/lib/4.0
 cd /var/lib/iHRIS/lib/4.0
 bzr branch lp:i2ce/4.0 I2CE
 bzr branch lp:ihris-common/4.0 ihris-common
 bzr branch lp:ihris-manage/4.0 ihris-manage
 bzr branch lp:textlayout/4.0 textlayout
These branches will always contain the latest release code.

===Development Code===
If you wish to work with the development code instead, you should do this:
 sudo mkdir -p /var/lib/iHRIS/lib/4.0-dev
 sudo chown -R `whoami`:`whoami` /var/lib/iHRIS/lib/4.0-dev
 cd /var/lib/iHRIS/lib/4.0-dev
 bzr branch lp:i2ce I2CE
 bzr branch lp:ihris-common ihris-common
 bzr branch lp:ihris-manage ihris-manage
 bzr branch lp:textlayout textlayout
These branches will always contain the main development code, which may or may be working at a particular time.

==Downloading CSSC's Customizations==
===Create a directory for Sites===
First we will create a directory that will hold all the sites we have on our system.  
 sudo mkdir -p /var/lib/iHRIS/sites/
 sudo chown -R `whoami`:`whoami` /var/lib/iHRIS/sites
We have two choices on how to download the CSSC Customizations.  One possibility to download it to ''install'' it, but do not want to make any code modifications.  The other possibility is to download the code and have it setup to modify the customizations.

===Download CSSC Customizations for no Modifications===
We can download the CSSC customizations to our site directory by doing:
 cd /var/lib/iHRIS/sites
 bzr branch lp:~ihris+cssc/ihris-manage/4.0-central cssc-central-4.0
You can still make modifications to the code, but they do not automatically get put back to launchpad once you commit.

===Download CSSC Customizations for Modification===
We can download the CSSC customizations to our site directory by doing:
 cd /var/lib/iHRIS/sites
 bzr checkout lp:~ihris+cssc/ihris-manage/4.0-central cssc-central-4.0
To see why we are doing a checkout instead of a branch, read [http://bazaar-vcs.org/CheckoutTutorial this].  To make sure everything is working OK, you should make sure the following succeeds:
 cd /var/lib/iHRIS/sites/cssc-central-4.0
 bzr commit -m "test commit"  --unchanged

==Creating the Database==
We will create a database called `cssc_central_4_0` as follows:
 mysql -u root -p 
 mysql> CREATE DATABASE `cssc_central_4_0`; 
 mysql> GRANT ALL PRIVILEGES ON `cssc_central_4_0`.* TO cssc@localhost identified by ''''PASSWORD''''; 
you should change '''PASSWORD''' to be the password you want.

==Installing on the Web Server==
Let us suppose we want to access the site at the URL:
 http://localhost/iHRIS/cssc-central

===Linking the Site===
First we will need to link to our customized site under '/var/www' as follows:
 sudo mkdir -p /var/www/iHRIS
 sudo ln -s /var/lib/iHRIS/sites/cssc-central-4.0/pages /var/www/iHRIS/cssc-central

===Setting the Database===
We will need to specify the database and database user/password we are using.  To do so:
 mkdir -p /var/lib/iHRIS/sites/cssc-central-4.0/pages/local
 cp /var/lib/iHRIS/sites/cssc-central-4.0/pages/config.values.php /var/lib/iHRIS/sites/cssc-central-4.0/pages/local/config.values.php
 gedit /var/lib/iHRIS/sites/cssc-central-4.0/pages/local/config.values.php
Look for the the following variables and set their values:
<center>
<table border='1' padding='2'>
<tr><th> Variable Name </th><th> Value</th></tr>
<tr><td>  $i2ce_site_i2ce_path </td><td> /var/lib/iHRIS/lib/4.0/I2CE </td></tr>
<tr><td> $i2ce_site_database </td><td> cssc_central_4_0 </td></tr>
<tr><td> $i2ce_site_database_user  </td><td> cssc </td></tr>
<tr><td> $i2ce_site_database_password  </td><td> '''PASSWORD''' (the password you set above) </td></tr>
</table>
</center>

===Finishing Up===
Just browse to the site at the URL:
 http://localhost/iHRIS/cssc-central
to begin the iHRIS installation process.

==Modifying the Code==
When you make changes to the code, you should do so in small steps with a message about what you have done.  This will help other developer's understand what you have done and to help track down bugs.  This process is called ''commit''ing.
 bzr help commit
===Ignored Files===
Anything in a directory named ''local'' is ignored.  
 bzr help ignore
 cd /var/lib/iHRIS/sites/cssc-central-4.0
 bzr ignore
This is why in  the above we copied config.values.php to local/config.values.php and set the database user name and password here.  This way, if we are modifying the CSSC customizations we don't need to worry about the user name and password being uploaded to launchpad.


===Updating files===
If you are working with many people on a site customization, you can get the changes that they have made using the 'bzr update' command.  For example:
 cd /var/lib/iHRIS/sites/cssc-central-4.0
 bzr update

===Changed Files===
To see which files have changed since the last time someone commited:
 cd /var/lib/iHRIS/sites/cssc-central-4.0
 bzr status

===Committing Code===
For instructions see:
 bzr help commit.


==Command Line Editors==
You may find that you will need to be able to edit a file from the command line, for example if you ssh into an iHRIS Appliance. There are several command line editors available that you can use to edit files and you should be familiar with at least one of them.
*emacs: powerful but not userfriendly (Carl's choice)
*vim: powerful but not userfriendly (Luke's choice)
*nano: Nano is by the far the easiest one to use, but is not very powerful and you can only work with one file at a time:

===Nano===
*to open a file to edit, type ''nano the_file_name.php'' on the command line
*to determine the line number you hit ''[CTRL]-C''
*Goto a line number ''[CTRL]-_''
*save files with ''[CTRL]-O''
*search for text with  ''[CTRL]-W''
*to cute (delete) a line ''[CTRL]-K''
*to paste the line(s) you just cut ''[CTRL]-U''
*if you decide to do a lot of editing in nano, you may want  to add syntax highlighting.   you can so as follows:
 nano ~/.nanorc
and save the following:
<source lang='text'>
## Sample initialization file for GNU nano.
##
## Please note that you must have configured nano with --enable-nanorc
## for this file to be read!  Also note that this file should not be in
## DOS or Mac format, and that characters specially interpreted by the
## shell should not be escaped here.
##
## To make sure a value is disabled, use "unset <option>".
##
## For the options that take parameters, the default value is given.
## Other options are unset by default.
##
## Quotes inside string parameters don't have to be escaped with
## backslashes.  The last double quote in the string will be treated as
## its end.  For example, for the "brackets" option, ""')>]}" will match
## ", ', ), >, ], and }.

## Use auto-indentation.
set autoindent

## Backup files to filename~.
set backup

## The directory to put unique backup files in.
# set backupdir ""

## Do backwards searches by default.
# set backwards

## Use bold text instead of reverse video text.
set boldtext

## The characters treated as closing brackets when justifying
## paragraphs.  They cannot contain blank characters.  Only closing
## punctuation, optionally followed by closing brackets, can end
## sentences.
##
set brackets ""')>]}"

## Do case sensitive searches by default.
# set casesensitive

## Constantly display the cursor position in the statusbar.  Note that
## this overrides "quickblank".
set const

## Use cut to end of line by default.
# set cut

## Set the line length for wrapping text and justifying paragraphs.
## If fill is 0 or less, the line length will be the screen width less
## this number.
##
#set fill -8

## Enable ~/.nano_history for saving and reading search/replace strings.
set historylog

## The opening and closing brackets that can be found by bracket
## searches.  They cannot contain blank characters.  The former set must
## come before the latter set, and both must be in the same order.
##
set matchbrackets "(<[{)>]}"

## Use the blank line below the titlebar as extra editing space.
# set morespace

## Enable mouse support, if available for your system.  When enabled,
## mouse clicks can be used to place the cursor, set the mark (with a
## double click), and execute shortcuts.  The mouse will work in the X
## Window System, and on the console when gpm is running.
##
set mouse

## Allow multiple file buffers (inserting a file will put it into a
## separate buffer).  You must have configured with --enable-multibuffer
## for this to work.
##
# set multibuffer

## Don't convert files from DOS/Mac format.
# set noconvert

## Don't follow symlinks when writing files.
# set nofollow

## Don't display the helpful shortcut lists at the bottom of the screen.
# set nohelp

## Don't add newlines to the ends of files.
set nonewlines

## Don't wrap text at all.
set nowrap

## Set operating directory.  nano will not read or write files outside
## this directory and its subdirectories.  Also, the current directory
## is changed to here, so any files are inserted from this dir.  A blank
## string means the operating directory feature is turned off.
##
# set operatingdir ""

## Preserve the XON and XOFF keys (^Q and ^S).
# set preserve

## The characters treated as closing punctuation when justifying
## paragraphs.  They cannot contain blank characters.  Only closing
## punctuation, optionally followed by closing brackets, can end
## sentences.
##
# set punct "!.?"

## Do quick statusbar blanking.  Statusbar messages will disappear after
## 1 keystroke instead of 26.  Note that "const" overrides this.
##
# set quickblank

## The email-quote string, used to justify email-quoted paragraphs.
## This is an extended regular expression if your system supports them,
## otherwise a literal string.  Default:
# set quotestr "^([ 	]*[#:>\|}])+"
## if you have extended regular expression support, otherwise:
# set quotestr "> "

## Fix Backspace/Delete confusion problem.
# set rebinddelete

## Fix numeric keypad key confusion problem.
# set rebindkeypad

## Do extended regular expression searches by default.
#set regexp

## Make the Home key smarter.  When Home is pressed anywhere but at the
## very beginning of non-whitespace characters on a line, the cursor
## will jump to that beginning (either forwards or backwards).  If the
## cursor is already at that position, it will jump to the true
## beginning of the line.
# set smarthome

## Use smooth scrolling as the default.
# set smooth

## Use this spelling checker instead of the internal one.  This option
## does not properly have a default value.
##
set speller "aspell -x -c"

## Allow nano to be suspended.
set suspend

## Use this tab size instead of the default; it must be greater than 0.
set tabsize 4

## Convert typed tabs to spaces.
set tabstospaces

## Save automatically on exit, don't prompt.
# set tempfile

## Disallow file modification; why would you want this in an rcfile? ;)
# set view

## The two single-column characters used to display the first characters
## of tabs and spaces.  187 in ISO 8859-1 (0000BB in Unicode) and 183 in
## ISO-8859-1 (0000B7 in Unicode) seem to be good values for these.
set whitespace ". "

## Detect word boundaries more accurately by treating punctuation
## characters as part of a word.
# set wordbounds

## Here is an example for PHP
##
syntax "php" "\.php[2345s~]?$"

## php markings
color brightgreen "(<\?(php)?|\?>)"

## functions
color white "\<[a-z_]*\("

## types
color green "\<(var|float|global|double|bool|char|int|enum|const)\>"

## structure
color brightyellow "\<(class|new|private|public|function|for|foreach|if|while|do|else|elseif|case|default|switch)\>"

## control flow
color magenta "\<(goto|continue|break|return)\>"

## strings
color brightyellow "<[^= ]*>" ""(\.|[^"])*""

## comments
color brightblue "//.*"
color brightblue start="/\*" end="\*/"
#color blue start="<" end=">"
#color red "&[^;[[:space:]]]*;"

## Trailing whitespace
color ,green "[[:space:]]+$"

include "/usr/share/nano/html.nanorc"

 ##############################################################################
#
# Syntax highlighting for XML files
#
# Author:  Josef 'Jupp' Schugt, jupp(a)rubyforge.org
# License: GPL 2  or later
#
# Version: 2004-02-25
#
##############################################################################

syntax "ml" ".*\.([jrs]?html?|xml|sgml?|lhtml|opml|kdevelop|vcproj|glade|xsd|plist|gcs|dtd|dcl)$" "catalog$" "docbook$"
color white "^.+$"
color green  start="<" end=">"
color cyan   "<[^> ]+"
color cyan   ">"
color yellow start="<!DOCTYPE" end="[/]?>"
color yellow start="<!--" end="-->"
color red    "&[^;]*;"

### all *js files  ( e.g. Firefox user.js, prefs.js )


## New updated taken from http://wiki.linuxhelp.net/index.php/Nano_Syntax_Highlighting

syntax "JavaScript" "\.(js)$"
## Default
color white "^.+$"
## Decimal, cotal and hexadecimal numbers
color yellow "\<[-+]?([1-9][0-9]*|0[0-7]*|0x[0-9a-fA-F]+)([uU][lL]?|[lL][uU]?)?\>"
## Floating point number with at least one digit before decimal point
color yellow "\<[-+]?([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)([EePp][+-]?[0-9]+)?[fFlL]?"
color yellow "\<[-+]?([0-9]+[EePp][+-]?[0-9]+)[fFlL]?"
## Keywords
color green "\<(break|case|catch|continue|default|delete|do|else|finally)\>"
color green "\<(for|function|if|in|instanceof|new|null|return|switch)\>"
color green "\<(switch|this|throw|try|typeof|undefined|var|void|while|with)\>"
## Type specifiers
color red "\<(Array|Boolean|Date|Enumerator|Error|Function|Math)\>"
color red "\<(Number|Object|RegExp|String)\>"
color red "\<(true|false)\>"
## String
color brightyellow "L?\"(\\"|[^"])*\""
color brightyellow "L?'(\'|[^'])*'"
## Escapes
color red "\\[0-7][0-7]?[0-7]?|\\x[0-9a-fA-F]+|\\[bfnrt'"\?\\]"
## Comments
color magenta start="/\*" end="\*/"
color magenta "//.*$"
</source>

==GUI Editors==
We don't use these so I don't have any recommendations.  You may want to look [https://help.ubuntu.com/community/Programming here] for some recommendations.
*gedit  Not geared to programming.  Installed by default on ubuntu desktop.
*[http://scintilla.org/SciTE.html scite] (sudo apt-get install scite)
Here are some IDEs
*geany A small GUI editor geared to programming (sudo apt-get install geany)
*[http://bluefish.openoffice.nl/features.html bluefish] (sudo apt-get install bluefish)
*eclipse

[[Category:Customizations]][[Category:Launchpad]][[Category:iHRIS Manage]][[Category:Review2013]]
