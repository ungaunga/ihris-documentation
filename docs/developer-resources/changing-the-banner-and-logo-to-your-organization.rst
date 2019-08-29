Changing the Banner and Logo to Your Organization
=================================================

In this tutorial we show how to change the banner, logo and other branding information to represent your organization.  This tutorial assumes that you have installed the *blank*  iHRIS Manage site according to these [[Linux (Ubuntu) Installation#Creating a Site Configuration File | directions]].



Changing the Header Text
^^^^^^^^^^^^^^^^^^^^^^^^
We will need to then modify **main.html** , one of the html template files which is in our site directory:
 sudo gedit /var/lib/iHRIS/sites/manage/templates/en_US/main.html
Now change the lines:


.. code-block:: xml

    <p id="siteName">iHRIS Manage</p>
    <p id="siteTag">Human Resource Management</p> 
    

to:


.. code-block:: xml

    <p id="siteName">iHRIS Manage -- Human Resource Management</p>
    <p id="siteTag">Ministry of Health - Taifeiki</p> 
    


Or whatever you feel is appropriate.


Changing the logo
^^^^^^^^^^^^^^^^^
Now we wish to change the logo, which is the green and blank iHRIS icon in the upper left hand side of the page.  Let us
suppose that you have already copied the image you want to use to your Desktop where it is called *my_logo.png* . Then
all you would need to do is:
  sudo mkdir -p /var/lib/iHRIS/sites/manage/images
  sudo cp ~/Desktop/my_logo.png /var/lib/iHRIS/sites/manage/images/iHRISManage_logo.png


Changing the banner image
^^^^^^^^^^^^^^^^^^^^^^^^^
Suppose you wish to change the banner image, which is by a woman leaning against a counter, with the file on your
desktop *my_picture.jpg*  then you would do:
 sudo mkdir -p /var/lib/iHRIS/sites/manage/images/photos
 sudo cp ~/Desktop/my_picture.jpg /var/lib/iHRIS/sites/manage/images/photos/loggedin_photo.jpg


