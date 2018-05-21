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


* [how-to-rewrite-urls-with-mod_rewrite-for-apache-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-rewrite-urls-with-mod_rewrite-for-apache-on-ubuntu-16-04)
```bash
sudo a2enmod rewrite && sudo service apache2 restart
```
* [Enable .htaccess under userdir](https://stackoverflow.com/questions/4289382/proper-userdir-conf-for-this-htaccess)
Edit: /etc/apache2/mods-enabled/userdir.conf then, restart apache
use option as illustrated:
AllowOverride All
```
vi /etc/apache2/mods-enabled/userdir.conf
#
<IfModule mod_userdir.c>
        UserDir public_html
        UserDir disabled root

        <Directory /home/*/public_html>
#               AllowOverride FileInfo AuthConfig Limit Indexes
                AllowOverride All
                Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
#                Options Indexes FollowSymLinks
                <Limit GET POST OPTIONS>
                        Require all granted
                </Limit>
                <LimitExcept GET POST OPTIONS>
                        Require all denied
                </LimitExcept>
        </Directory>
</IfModule>
#
# restart apache:
sudo service apache2 restart
```

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

### CGI
Add the following right after the first line, which reads <VirtualHost *:80\>.
```bash
#
sudo a2enmod cgi
#
sudo vi /etc/apache2/mods-available/php7.0.conf
#
<Directory /home/*/public_html/*/cgi-bin>
    Options +ExecCGI
    SetHandler cgi-script
    AddHandler cgi-script .py 
</Directory>
#
sudo service apache2 restart
```

### WSGI: mod_wsgi
- https://code.google.com/archive/p/modwsgi/wikis/QuickConfigurationGuide.wiki

**WSGI Application Script File**
WSGI is a specification of a generic API for mapping between an underlying web server and a Python web application. WSGI itself is described by Python PEP 0333. The purpose of the WSGI specification is to provide a common mechanism for hosting a Python web application on a range of different web servers supporting the Python programming language.

**Mounting The WSGI Application**
There are a number of ways that a WSGI application hosted by mod_wsgi can be mounted against a specific URL. These methods are similar to how one would configure traditional CGI applications.

Require **WSGI module**
```bash
sudo apt-get install libapache2-mod-wsgi python-dev
#
sudo a2enmod wsgi
```
-http://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIScriptAlias.html
```bash
<IfModule mod_userdir.c>
    <Directory /home/*/public_html>
        #php_admin_flag engine Off
    </Directory>
    <Directory /home/*/public_html/*/cgi-bin>
        Options +ExecCGI
        SetHandler cgi-script
        AddHandler cgi-script .py 
    </Directory>
    <Directory /home/*/public_html/*/wsgi-bin>
        Options +ExecCGI
        SetHandler wsgi-script
        AddHandler wsgi-script .wsgi
    </Directory>
</IfModule>
```

**Configuration files**
sudo vi /etc/apache2/sites-available/000-default.conf
sudo vi /etc/apache2/mods-enabled/userdir.conf
#
sudo vi /etc/apache2/mods-available/userdir.conf
```bash
<IfModule mod_userdir.c>
        UserDir public_html
        UserDir disabled root

        <Directory /home/*/public_html>
                #AllowOverride FileInfo AuthConfig Limit Indexes
                AllowOverride All
                Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
                <Limit GET POST OPTIONS>
                        Require all granted
                </Limit>
                <LimitExcept GET POST OPTIONS>
                        Require all denied
                </LimitExcept>
        </Directory>
        <Directory /home/*/public_html/*/cgi-bin>
                Options +ExecCGI
                SetHandler cgi-script
                AddHandler cgi-script .py
        </Directory>
        <Directory /home/*/public_html/*/wsgi-bin>
                #Order allow,deny
                #Allow from all
                Options +ExecCGI
                DirectoryIndex index.wsgi
                SetHandler wsgi-script
                AddHandler wsgi-script .wsgi
                WSGIScriptReloading On
        </Directory>
</IfModule>

```
- restart the server
```bash
sudo service apache2 restart
```
**Getting Started:mod_wsgi**
http://modwsgi.readthedocs.io/en/develop/getting-started.html

* **Note that mod_wsgi requires that the WSGI application entry point be called ‘application’**
* If you want to call it something else then you would need to configure mod_wsgi explicitly to use the other name. Thus, don’t go arbitrarily changing the name of the function. If you do, even if you set up everything else correctly the application will not be found.
* Both Python 2 and 3 are supported. The minimum recommended versions of each being Python 2.6 and 3.3 respectively.

**Sample Application with Flask**
http://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php
