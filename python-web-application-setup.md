---
title: Web Application Setup for Python
---

**Table of Contents**
* TOC
{:toc}


## Web Application Setup for Python
>Learning to setup Apache for web applications in python


Most of the ML and Deep Learning applications are written in python and often in a stand alone mode. We can complete the circle by creating the Web interface for the application and providing the REST interface for the core functionality.

You created a ML model to make som predictions, but only you the creator of the model can use it since it's only available on your machine.

- How do I implement this model in real life?
- How to implement a machine learning model using Flask framework in Python?
- How to deploy a machine learning model with Flask?
- How to persist our model so we can have access to it without always having to retrain it each time we want to make a prediction?
- What Flask is and how to set it up?

### References
- https://www.analyticsvidhya.com/blog/2017/09/machine-learning-models-as-apis-using-flask/
- https://www.wintellect.com/creating-machine-learning-web-api-flask/
- https://blog.hyperiondev.com/index.php/2018/02/01/deploy-machine-learning-model-flask-api/
- https://medium.com/@dvelsner/deploying-a-simple-machine-learning-model-in-a-modern-web-application-flask-angular-docker-a657db075280




## Apache2 Installation & Configuration
```bash
sudo apt-get install apache2 apache2-utils libexpat1 ssl-cert
#
Enable and Configure Apache2 Userdir Module in Ubuntu
#
# configuration
sudo a2enmod userdir
sudo service apache2 restart
mkdir ~/public_html && chmod 0755 ~/public_html
#
# comment out a line php_admin_value engine Off
#
sudo vi /etc/apache2/mods-available/php7.0.conf
#
sudo /etc/init.d/apache2 reload
echo '<?php phpinfo(); ?>' > ~/public_html/info.php
#
# Enable .htaccess under userdir
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

**WSGI Application Script File**
WSGI is a specification of a generic API for mapping between an underlying web server and a Python web application. WSGI itself is described by Python PEP 0333. The purpose of the WSGI specification is to provide a common mechanism for hosting a Python web application on a range of different web servers supporting the Python programming language.

**Mounting The WSGI Application**
There are a number of ways that a WSGI application hosted by mod_wsgi can be mounted against a specific URL. These methods are similar to how one would configure traditional CGI applications.

- http://ict.gctaa.net/summer/2011/userspace_wsgi.html

```bash
# disable multithreading processes
#
sudo a2dismod mpm_event
#
# give Apache explicit permission to run scripts
#
sudo a2enmod mpm_prefork cgi
# CGI and WSGI
sudo apt-get install libapache2-mod-wsgi python-dev
sudo a2enmod cgi
#
sudo a2enmod wsgi
#
sudo vi /etc/apache2/mods-available/php7.0.conf
#
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
#
sudo service apache2 restart
```

## Flask
http://flask.pocoo.org/
```
sudo pip2 install Flask
```

**with Apache**
- https://www.jakowicz.com/flask-apache-wsgi/
- https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask

- http://modwsgi.readthedocs.io/en/develop/user-guides/configuration-guidelines.html
```bash
webtool.wsgi
import sys
sys.path.append('/home/game/public_html/wsgi-bin')
from webtool import app as application

webtool.py
#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Python world :D!"

if __name__=="__main__":
	app.run(debug=True)
```
* http://jsonmate.com/


## WSGI Servers
- https://www.fullstackpython.com/wsgi-servers.html
- https://realpython.com/kickstarting-flask-on-ubuntu-setup-and-deployment/
```bash
sudo pip install gunicorn
sudo pip3 install gunicorn
#
gunicorn app:app -b localhost:8000
gunicorn index:app -b localhost:8080
```

https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server

http://2ality.com/2014/06/simple-http-server.html



https://stackoverflow.com/questions/10396330/how-to-host-python-cgi-script-with-python-m-simplehttpserver-8000-or-python

This work for me, run the python -m CGIHTTPServer 8000 command same menu level with cgi-bin,and move cgi_script.py into cgi-bin folder.In browser type http://localhost:8000/cgi-bin/cgi_script.py

https://gist.github.com/yoavram/4351498
https://blog.hyperiondev.com/index.php/2018/02/01/deploy-machine-learning-model-flask-api/


## Setup Env Variables
- https://github.com/theskumar/python-dotenv
- https://robinislam.me/blog/reading-environment-variables-in-python/