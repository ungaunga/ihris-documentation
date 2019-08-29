Installing iHRIS on Ubuntu 10.4 (Lucid)
=======================================

Ubuntu 10.4 and 10.10 come with PHP 5.3 so there a few a few issues that need to be corrected.

SEE: 
http://pecl.php.net/bugs/bug.php?id=16814 for a discussion of the issue.  It is not clear what the correct resolution is, but we try to offer some suggestions here.  

==Do I Have The Problem?==
You can tell if you are affected by this issue if you see the something like the following under apache_tail
<pre>
[Mon Dec 20 12:04:44 2010] [error] [client 127.0.0.1]
	I2CE: I2CE_Error->handleError (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE.php:858)
	      I2CE->handleError
	      apc_store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataStorageAPC.php:78)
	      I2CE_MagicDataStorageAPC->store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicData.php:155)
	      I2CE_MagicData->store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1423)
	      I2CE_MagicDataNode->save (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:978)
	      I2CE_MagicDataNode->newChild (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1079)
	      I2CE_MagicDataNode->traverse (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:994)
	      I2CE_MagicDataNode->__set (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:788)
	      I2CE_Updater->storeModuleMagicData (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:685)
	      I2CE_Updater->_updateModules (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:337)
	      I2CE_Updater->updateOutOfDateConfigFiles (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:148)
	      I2CE_Updater->_updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:50)
	      I2CE_Updater->updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE.php:600)
	      I2CE->initializeDSN (/home/litlfred/rocket_cats/sites/togo/pages/index.php:49)
	apc_store(): Potential cache slam averted for key 'I2CE_MD_manage_togo_config_data_4277bc096c759cba46d3810b3081d6d5'
	Occured on line 78 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataStorageAPC.php
[Mon Dec 20 12:04:44 2010] [error] [client 127.0.0.1]
	I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:2089)
	      I2CE_MagicDataNode->raiseError (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataStorageAPC.php:82)
	      I2CE_MagicDataStorageAPC->store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicData.php:155)
	      I2CE_MagicData->store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1423)
	      I2CE_MagicDataNode->save (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:978)
	      I2CE_MagicDataNode->newChild (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1079)
	      I2CE_MagicDataNode->traverse (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:994)
	      I2CE_MagicDataNode->__set (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:788)
	      I2CE_Updater->storeModuleMagicData (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:685)
	      I2CE_Updater->_updateModules (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:337)
	      I2CE_Updater->updateOutOfDateConfigFiles (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:148)
	      I2CE_Updater->_updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:50)
	      I2CE_Updater->updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE.php:600)
	      I2CE->initializeDSN (/home/litlfred/rocket_cats/sites/togo/pages/index.php:49)
	Error saving to APC config:I2CE/tasks/role_trickle_down Type: 0 Value:  Children: admin,exec_manager,hr_manager,training_manager,hr_staff
	Called from I2CE_MagicDataStorageAPC->store() at line 155 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicData.php
	Called from I2CE_MagicData->store() at line 1423 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php
	Called from I2CE_MagicDataNode->save() at line 978 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php
	Called from I2CE_MagicDataNode->newChild() at line 1079 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php
	Called from I2CE_MagicDataNode->traverse() at line 994 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php
	Called from I2CE_MagicDataNode->__set() at line 788 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php
	Called from I2CE_Updater::storeModuleMagicData() at line 685 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php
	Called from I2CE_Updater::_updateModules() at line 337 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php
	Called from I2CE_Updater::updateOutOfDateConfigFiles() at line 148 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php
	Called from I2CE_Updater::_updateSite() at line 50 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php
	Called from I2CE_Updater::updateSite() at line 600 of /home/litlfred/rocket_cats/dev/I2CE/lib/I2CE.php
	Called from I2CE::initializeDSN() at line 49 of /home/litlfred/rocket_cats/sites/togo/pages/index.php
[Mon Dec 20 12:04:44 2010] [error] [client 127.0.0.1]
	I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicData.php:157)
	      I2CE_MagicData->store (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1423)
	      I2CE_MagicDataNode->save (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:978)
	      I2CE_MagicDataNode->newChild (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:1079)
	      I2CE_MagicDataNode->traverse (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_MagicDataNode.php:994)
	      I2CE_MagicDataNode->__set (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:788)
	      I2CE_Updater->storeModuleMagicData (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:685)
	      I2CE_Updater->_updateModules (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:337)
	      I2CE_Updater->updateOutOfDateConfigFiles (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:148)
	      I2CE_Updater->_updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE_Updater.php:50)
	      I2CE_Updater->updateSite (/home/litlfred/rocket_cats/dev/I2CE/lib/I2CE.php:600)
	      I2CE->initializeDSN (/home/litlfred/rocket_cats/sites/togo/pages/index.php:49)
	Failed to store for 0: I2CE_MagicDataStorageAPC

</pre>

==Simple Install==
===Command Line===
<source lang='bash'>
sudo add-apt-repository ppa:chris-lea/php-pecl-extras
sudo apt-get update
sudo apt-get install php5-apc
</source>

===GUI===
Go to "System"->"Administration"->"Synaptic Package Manager"->"Settings"->"Repositories"->"Other Software"->"Add..."
*Add the following APT Line For Maverick Meerkat (10.10) : 
 deb http://ppa.launchpad.net/chris-lea/php-pecl-extras/ubuntu maverick main 
*Add the following APT Line For For Lucid Lynx (10.04)
 deb http://ppa.launchpad.net/chris-lea/php-pecl-extras/ubuntu lucid main 

Now "Close" and "Reload" and you can install the php5-apc package.

==Manual Install==

To compile pecl packages yourself you'll need these packages installed.  They may already be installed.
<source lang="bash">
sudo apt-get install php5-dev apache2-prefork-dev
</source>

The version of APC that ships with 10.4 and 10.10 causes problems.  You'll need to downgrade it for it to work.  When it asks if you want to use the spin locks type in yes.  Run the following commands in a terminal:
===For Lucid (10.04)===
<source lang="bash">
sudo apt-get remove php-apc
sudo pecl config-set preferred_state beta
sudo pecl install APC-3.1.5
sudo pecl config-set preferred_state stable
</source>
You may also want to try the steps for Meerkat (below)

===For Meerkat (10.10)===
This seems to work as of Dec 20, 2010.
<source lang="bash">
sudo apt-get remove php-apc
sudo pecl install APC
</source>

Now you need to set the configuration options for APC.  Create or edit the ini file by typing:
<source lang="bash">
sudo gedit /etc/php5/conf.d/apc.ini
</source>

The contents should be:
<source lang="ini">
extension=apc.so
apc.shm_size=100M
apc.write_lock=1
apc.slam_defense=0
</source>

==Restart==

Now restart apache and memcached (if you're using it) and try to access your site again.
<source lang="bash">
sudo /etc/init.d/apache2 restart
sudo /etc/init.d/memcached restart
</source>


==Version Stuff==
Updated Dec 20, 2010:
===PECL===
*[http://pecl.php.net/package/APC Stable] is 3.1.6 Released Nov 20, 2010 -- I think it is OK here
===Ubuntu===
*Meerkat [https://launchpad.net/ubuntu/maverick/+source/php-apc source] is 3.1.3p1-2  -- It is no good here
*Lucid [https://launchpad.net/ubuntu/lucid/+source/php-apc source] is 3.1.3p1-2 -- It is no good here
*Jaunty [https://launchpad.net/ubuntu/jaunty/+source/php-apc source] php-apc 3.0.19-2  -- I think it is OK here.

[[Category:Developer Resources]]
