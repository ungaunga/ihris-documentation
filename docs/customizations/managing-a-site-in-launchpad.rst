Managing A Site In Launchpad
================================================

This tutorial will take you through the steps of managing a site via bazaar on Launchpad based on some customizations that you have already made on your Ubuntu machine for version 4.0 of iHRIS Qualify for the Nursing and Midwives Council.

We will assume that, for the purposes of this tutorial, that the existing customizations live under 
 /var/lib/iHRIS/sites/qualify

We need to make sure thae bazaar version control software is installed.  Then  we will  setup a user account on launchpad and connect it to the account on your machine.  We will also  create a team to manage the customizations. 



Setting up Bazaar
^^^^^^^^^^^^^^^^^
First we need to make sure the `Bazaaar <http://bazaar-vcs.org/en/>`_ (bzr) version control software is installed:
  sudo apt-get install bzr bzrtools
You may wish to read the `five minute tutorial <http://doc.bazaar-vcs.org/latest/en/mini-tutorial/index.html>`_ at this point.  You should also let bzr know how you are:
  bzr whoami "'''Your Name <your@email.add.ress>'''"



Creating a Launchpad Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First you should create an account on `Launchpad <https://launchpad.net/>`_. If you not have already done so, you can find some help `here <https://help.launchpad.net/YourAccount/NewAccount>`_. 

We will refer to this account as **LAUNCHPAD_USER.**


Creating a Launchpad Team
^^^^^^^^^^^^^^^^^^^^^^^^^

Presumably, you will want to have several people be able to update the customizations you are storing on Launchpad.  This is done by creating a team.  To do so:


* Browse to the launchpad `homepage <https://launchpad.net/>`_
* Select "Register a Team"
* *For the *Name* I suggest something like *ihris-*'COUNTRY_NAME''''' or *ihris-*'ORGANIZATION_NAME'''''
* *For the *Display Name* you can use something like *iHRIS in **COUNTRY_NAME***
* *For the Subscription policy, I suggest making it "Open"
Once the team is created, you can choose view its home page at 
  *<nowiki>https://www.launchpad.net/~ihris-</nowiki>*'COUNTRY_NAME''''' 
To change some of it's details, browse to the team home page where you can:


* Add members to the team by the "Add Member" Link
* Change the owner of the team by "Change Details," scroll to the bottom, "Change Owner"
* Change the logo/icon for the team by "Change Details," scroll to the bottom, "Change Branding"


Adding Intrahealth Informatics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may also wish to give the *intrahealth-informatics* team as a member of to the team you just created.  This will enable the people in this team to edit the customizations


Linking your Launchpad Account to your Ubuntu Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since we will want to contribute to the code, we need to let Launchpad know who are.  To do this, we create a `ssh public key <https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair>`_ on your Ubuntu machine to add to Launchpad:
 sudo apt-get install openssh-client
 ssh-keygen -t rsa
When prompted, press Enter to accept the default file name for your key. Next, enter then confirm a password to protect your SSH key.  

Your key pair is now stored in ~/.ssh/id_rsa.pub (public key) and ~/.ssh/id_rsa (private key). Now you need to upload the public portion of your SSH key to Launchpad. To do this, open in your web browser:
 <nowiki>https://www.launchpad.net/~</nowiki>'''LAUNCHPAD_USER'''
You will see a place that says *SSH Keys* with an exclamation point **(!)** in a yellow circle next to it.  Click on the **(!)** scroll down until you see *Add an SSH Key* and a text box.  We will paste our public key into this text box.  To do so type in a terminal:
 gedit ~/.ssh/id_rsa.pub
you can now copy the contents of gedit (the public key) into the text box in the web browser.  Now simply click on the button *Import Public Key*

 **Note:** For every computer/account that you use you will need to repeat these steps to create and import a public key.


Creating A Project
^^^^^^^^^^^^^^^^^^
The team is used to manage who can access the code.  Now we need to create a place, or project, to handle these and any future customizations for iHRIS Qualify for the Nursing Council.  To do so:


* Browse to the Launchpad home page https://www.launchpad.net/
* Select "Register a Project" with the details:
* *Step 1
* **Name is *ihris+nmc+*'COUNTRY_NAME'''
* **Title is *iHRIS Qualify for NMC in **COUNTRY_NAME***
* **Summary is *Implementation of iHRIS Qualify for the Nursing and Midwifery Council of **COUNTRY_NAME***
* *Step 2
* **Click "No, this is a new Project"
* **For the License, check "GNU GPL V3"
* **Click "Complete Registration"

You project now has its home page at
 <nowiki>https://edge.launchpad.net/ihris+nmc+</nowiki>'''COUNTRY_NAME'''
From the project home page you can:


* Change the Maintainer by clicking the exclamation point yellow circle next to "Maintainer".  You should set it to be the team *ihris-*'COUNTRY_NAME''' that you created above
* Change the branding (icon)
* Edit the project details and set it to be "Part of:" the 'ihris-suite' project


Creating a Branch
^^^^^^^^^^^^^^^^^
A "branch" is where the actual code is hosted in the project.  You may want to have several branches to keep track of the different versions of the iHRIS Qualify software as it get's updated.  The primary branch is the "trunk" which will be working with here.  We will need to create this on Launchpad by clicking on the "Code" tab under the projects's home page.  This should take you to:
 *<nowiki>https://code.launchpad.net/ihris+nmc+</nowiki>*'COUNTRY_NAME'''
We will create a branch to handle the customizations of version 4.0 of iHRIS Qualify for the Nursing and Midwives council by:


* Select "Register A Branch" with the following details:
* *For the owner, make sure it is the team we created above *ihris-*'COUNTRY_NAME'''''
* *For the "Name" use  "NMC-4.0"  is short for Nursing and Midwifery Council version 4.0
* *Branch Type is "Hosted"
* *Status is "Development"

The branch's home page is now:
 <nowiki>https://code.edge.launchpad.net/~ihris-</nowiki>'''COUNTRY_NAME'''/ihris+nmc+'''COUNTRY_NAME'''/NMC-4.0

We wish to set this branch to be the main place to commit code for our project.  To do so:


* Go to the projects home page
* select the "Code" tab and
* click "Set the Development Focus" and set:
* *The branch to be: ~ihris-'''COUNTRY_NAME'''/ihris+nmc+'''COUNTRY_NAME'''/NMC-4.0


Adding your Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^
To actually put our code customizations on Launchpad we do:
 cd /var/lib/iHRIS/sites/qualify
 bzr init
 bzr push lp:ihris+nmc+'''COUNTRY_NAME''' --use-existing-dir
 bzr bind lp:ihris+nmc+'''COUNTRY_NAME''' 
which tells our computer that the customizations under /var/lib/iHRIS/site/qualify should be the same as the code on launchpad. To actually put the code on Launchpad, we will need to add in the files for our customization and make our first "commit:"
 cd /var/lib/iHRIS/sites/qualify
 bzr add
 bzr commit -m  "Initial Upload"
Here the *-m "Initial Upload"* is a short message describing that this is first *commit* of the branch.


Making more Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^
Suppose that we changed one of the .html template files we can commit them to Launchpad by:
 cd /var/lib/iHRIS/sites/qualify
 bzr commit -m "Changed the main page header"



Updating the Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are working on multiple machines or with multiple people, you may want to get the committed changes to the customizations onto your computer.  You can do this by:
 cd /var/lib/iHRIS/sites/qualify
 bzr update

[[Category:iHRIS Qualify]][[Category:Customizations]][[Category:Launchpad]][[Category:Review2013]]
