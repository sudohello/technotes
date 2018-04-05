/*
Title: Apache Guide
Decription: Apache
Author: Bhaskar Mangal
Date: 
Tags: Apache Guide
*/

# Apache Guide

## Apache2 Installation

* Install Webserver (Apache2)
```
sudo apt-get install apache2
```

* Check the service status on Ubuntu
```
sudo service --status-all
```

* Restart apache2 service:
```
sudo service apache2 restart
```

* Check in the browser:
http://localhost/

* Apache2 Ubuntu Default Page should display. The configuration layout for an Apache2 web server installation on Ubuntu systems is as follows:
```
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
```

* Apache Logs
```
ls /var/log/apache2/
tail -f /var/log/apache2/error.log
```

* Configuration
```
gvim /etc/apache2/sites-available/000-default.conf
```

* [How to Enable and Configure Apache2 Userdir Module in Ubuntu Server?](http://ubuntuserverguide.com/2012/10/how-to-enable-and-configure-apache2-userdir-module-in-ubuntu-server-12-04.html)
  - Apache2 userdir module is used to create a webroot in the user’s home directory
  - By using userdir module each user that is in the system will have the Apache2 root directory with the folder name public_html  in the home directory
  - If you using any web browser to access the webroot folder in the user directory you should use the “~” afterwards username. So, the url address to be http://[hostname]/~username/
  - By default Userdir Module is available when apache2 package installed on ubuntu server but not yet active. We just need to enable userdir module to be used.
```bash
sudo a2enmod userdir
sudo service apache2 restart
mkdir ~/public_html && chmod 0755 ~/public_html
#
# comment out a line php_admin_value engine Off
sudo vi /etc/apache2/mods-available/php7.0.conf
#
#
sudo /etc/init.d/apache2 reload
echo '<?php phpinfo(); ?>' > ~/public_html/info.php
```
**Apache2 Userdir Module Support PHP Script**
sudo vi /etc/apache2/mods-available/php5.conf
Now you need to comment out a line php_admin_value engine Off

## Python with Apache
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04

```bash
# disable multithreading processes
#
sudo a2dismod mpm_event
#
# give Apache explicit permission to run scripts
#
sudo a2enmod mpm_prefork cgi
#
# modify the actual Apache configuration, to explicitly declare Python files as runnable file and allow such executables
#
sudo vi /etc/apache2/sites-enabled/000-default.conf
```

Add the following right after the first line, which reads <VirtualHost *:80\>.
```bash
#
sudo a2enmod cgi
#
sudo vi sudo vi /etc/apache2/mods-available/php7.0.conf
#
<Directory /home/*/public_html/*/cgi-bin>
    Options +ExecCGI
    SetHandler cgi-script
    AddHandler cgi-script .py 
</Directory>
#
sudo service apache2 restart
```

