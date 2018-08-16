/*
Title: MySQL
Decription: MySQL
Author: Bhaskar Mangal
Date: 07th May 2018
Tags: MySQL
*/


## MySQL
- https://websiteforstudents.com/install-mysql-latest-versions-on-ubuntu-16-04-lts-server/
- http://www.codingpedia.org/ama/how-to-install-mysql-server-5-7-on-ubuntu-16-04
```bash
sudo apt-get install mysql-server
sudo apt install mysql-workbench
mysql-workbench
mysql --version
sudo service mysql status
```
* Aliases
```bash
# MySql
alias mysql-start="sudo service mysql start"
alias mysql-stop="sudo service mysql stop"
alias mysql-restart="sudo service mysql restart"
alias mysql-status="sudo service mysql status"
alias mysql-connect-root="mysql -uroot -p"
alias mysql-vim-mysql.conf.d.my.cnf="sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf"
```
* Configuration Files
```
/etc/mysql/
|-- conf.d
|   -- mysql.cnf
|-- my.cnf -> /etc/alternatives/my.cnf
|-- my.cnf.fallback
|-- mysql.cnf
|-- mysql.cnf.2017-01-13-original
|-- mysql.conf.d
    -- mysqld.cnf
```
**Re-setting root password**
- https://stackoverflow.com/questions/16556497/how-to-reset-or-change-the-mysql-root-password
```bash
# find mysql server version
dpkg --get-selections | grep mysql-server
# reset
sudo dpkg-reconfigure mysql-server-5.7
sudo mysql_secure_installation
sudo ufw allow 3306/tcp
sudo service ufw restart
```


sudo apt install flashplugin-installer