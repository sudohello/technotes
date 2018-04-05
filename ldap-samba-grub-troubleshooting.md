/*
Title: Grub LDAP Samba
Decription: Grub LDAP Samba
Author: Bhaskar Mangal
Date: 
Tags: Grub LDAP Samba
*/


# Grub LDAP Samba

## Recovering LDAP and other server configuration after Hard Server Stop!
We had two system:

* **Ser1: NFS mounted, CentOS-5.10**
  - after manual restart, it got stuck during boot
  - single user mode through passing the param to grub loader, and stoping the services that were causing trouble. These services won't show up again during boot process
  - used interactive session during boot to manually skip the service that were still causing trouble

* **Ser2: LDAP, Samba Server, Ubuntu-14.04**
  - after hard stop, it got stuck during boot
  - used Ubuntu 16.04 live USB to boot for:
    - to access the filesystem for complete backup
    - chroot to the root and run the ldap scripts to get the LDAP data backup
  - formatted the system and installed ubuntu 16.04
  - LDAP setup
  - Samba server setup
  - Samba configuration for LDAP
* **Note**:
	- replace `blah` with the domain-name

After hard reset, Ser2 (Ububtu) get's stucks's during booting at **hangs after "Begin: Running /scripts/init-bottom".**
* [ubuntu-hangs-after-begin-running-scripts-init-bottom-done](https://askubuntu.com/questions/521831/ubuntu-server-vm-hangs-after-begin-running-scripts-init-bottom-done)

No matter, what I tried, Ser2 did not boot. I'd tried following:-
1. grub-installation, grub-update
2. Filesystem Check, [Force File system check](https://www.cyberciti.biz/faq/linux-force-fsck-on-the-next-reboot-or-boot-sequence/)
```bash
sudo touch /forcefsck
```
3. [Update initramfs](https://ubuntugenius.wordpress.com/2010/05/24/fix-a-failed-initramfs-update-do-it-before-you-reboot/)
```bash
update-initramfs -u
update-initramfs -u -k all
```
* displayed the scripts that ran at startup with
  - [scripts-slowing-boot](https://askubuntu.com/questions/177299/scripts-slowing-boot)
```bash
initctl list
#
/usr/share/initramfs-tools/init
```
* [kernel-newbie-corner-initrd-and-initramfs-whats](https://www.linux.com/learn/kernel-newbie-corner-initrd-and-initramfs-whats)
  - ideas of initrd and initramfs, and what they're for and, most importantly
  - **initrd - initial ram disk**
    - the bootloader's job to pass control to the kernel, hand it the "initrd" (initial ram disk), let the kernel mount it and get what it needs, whereupon the kernel can toss the initrd and replace it with the real root filesystem.
  - **initramfs (initial RAM file system)**
    - It is what I call an even earlier potential root file system that you can build into the kernel image itself. And because of its location (internal to the kernel), it will (if it exists) take precedence.
The initial RAM filesystem is a ramfs which is loaded by the boot loader (loadlin or lilo) and that is mounted as root before the normal boot procedure. It is typically used to load modules needed to mount the "real" root file system, etc.

And some other ad-hoc things were done, with no benefits. Finally, we decided to format the Ser2, but we still need to get the backup of the LDAP server.

**How we can take the backup of the LDAP server data when the Server on which it was installed was not booting up?**

By now I was convinced that the filesystem was intact, so that we can take the LDAP data backup. We used the bootable USB to boot to ubuntu 16.04 and chroot to the partition

```bash
mkdir /mnt/sda1
sudo mount -o rw /dev/sda1 /mnt/sda1
sudo mount --bind /dev /mnt/sda1/dev
sudo mount --bind /dev/pts /mnt/sda1/dev/pts
sudo mount --bind /proc /mnt/sda1/proc
sudo mount --bind /sys /mnt/sda1/sys
sudo chroot /mnt/sda1
#
sudo -i
##----------
# Updating initramfs did not resolve booting issue
update-initramfs -c -k x.x.x-xx-generic
#for example if your kernel system 4.4.0-31-generic
update-initramfs -c -k 4.4.0-31-generic
# 
dpkg –configure -a
apt-get update
##----------
slapd -l bkup.ldiff
# To exit from chroot
exit
# before restarting the system, unmount individually
umount /mnt/sda1/sys
umount /mnt/sda1/proc
umount /mnt/sda1/dev/pts
umount /mnt/sda1/dev
umount /mnt/sda1
#
reboot
```

## Ser2 - LDAP Installation
Refer the following link to install the LDAP, samba-ldap

### References
* [install-configure-openldap-server-ubuntu-16-04](https://www.linuxbabe.com/ubuntu/install-configure-openldap-server-ubuntu-16-04)
* [openldap-server.html#openldap-configuration](https://help.ubuntu.com/lts/serverguide/openldap-server.html#openldap-configuration)
* [samba-ldap](https://help.ubuntu.com/lts/serverguide/samba-ldap.html)
* [samba-introduction](https://help.ubuntu.com/lts/serverguide/samba-introduction.html)
* [LDAB vocabulary](http://www.zytrax.com/books/ldap/ape/)
* [getent](http://www.commandlinefu.com/commands/using/getent)

### Installation
* **Basic toolchain setup**
```bash
sudo apt-get update
sudo apt-get install -y openssh-server openssh-client
sudo apt-get install -y vim-gtk
sudo apt-get install -y tkcvs
```
* **Install LDAP**
	* slapd - Stand-Alone LDAP Daemon.
```bash
# You will be asked to set a password for the admin entry in the LDAP directory
sudo apt-get install slapd ldap-utils
```
	* Basic Post-Installation Configuration
```bash
sudo dpkg-reconfigure slapd
```
	* ldap directory after install will be `/etc/ldap`. Verify the LDAP, default listening post for LDAP server is `389`
```bash
sudo netstat -antup | grep -i 389
```

* **Install phpldapadmin**
	- php basesd admin utility
```bash
apt-get install apache2
sudo apt-get install php7.0 php7.0-gd libapache2-mod-php7.0
apt-get install phpldapadmin
```
* **Install misc schema**
	* misc schema is needed for nisMapAlias and other related attribute/objectClass
```bash
#download misc schema ldif
wget https://raw.githubusercontent.com/openshift/openldap/master/2.4.41/contrib/config/schema/misc.ldif
#to import misc schema to ldap
cat misc.ldif | sudo ldapadd -Q -Y EXTERNAL -H ldapi:///
#to query and view the new schema
sudo ldapsearch -Q -LLL -Y EXTERNAL -H ldapi:/// -b cn=schema,cn=config 'cn=*misc*'
```
* **Install Samba and Samba LDAP**
	- to enable samba support for LDAP, samba schema is required. Install samba server and samba tools, import the samba schema to LDAP
```bash
apt-get install samba smbldap-tools
```
	* to configure samba server open /etc/samba/smb.conf and change the workgroup from default value of `WORKGROUP` to required value for `workgroup = WORKGROUP`

	**++Samba LDAP Configuration++**

	1. Import Samba Schema
```bash
zcat /usr/share/doc/samba/examples/LDAP/samba.ldif.gz | sudo ldapadd -Q -Y EXTERNAL -H ldapi:///
# to query and view the new schema
sudo ldapsearch -Q -LLL -Y EXTERNAL -H ldapi:/// -b cn=schema,cn=config 'cn=*samba*'
```
	2. Create Samba indices
		- Create the file samba_indices.ldif with the following contents:
		- Note: we are using **hdb** database and not the default **mdb**
		- Create file at: `/etc/ldap/schema/samba_indices.ldif`
	```bash
dn: olcDatabase={1}hdb,cn=config
changetype: modify
replace: olcDbIndex
olcDbIndex: objectClass eq
olcDbIndex: uidNumber eq
olcDbIndex: gidNumber eq
olcDbIndex: loginShell eq
olcDbIndex: uid eq,pres,sub
olcDbIndex: cn eq,pres,sub
olcDbIndex: memberUid eq,pres,sub
olcDbIndex: uniqueMember eq,pres
olcDbIndex: sambaSID eq
olcDbIndex: sambaPrimaryGroupSID eq
olcDbIndex: sambaGroupType eq
olcDbIndex: sambaSIDList eq
olcDbIndex: sambaDomainName eq
olcDbIndex: default sub,eq
```
		- Using the **ldapmodify** utility load the new indices
```bash
sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f samba_indices.ldif
```
	3. Verify new Indices
		- Using the **ldapsearch** utility query the new indices
```bash
#
sudo ldapsearch -Q -LLL -Y EXTERNAL -H  ldapi:/// -b cn=config olcDatabase={1}hdb olcDbIndex
#
ldapsearch -D the-dn-you-use -w -the-password-you-use -H <IP>:389 -s base -b dc=example,dc=com '(&)' 1.1
#
ldapsearch -D "cn=admin,cn=People,dc=blah,dc=com" -H <IP>:389 -s base -b dc=blah,dc=com '(&)' 1.1
#
ldapsearch -D "uid=<userName>,ou=People,dc=blah,dc=com" -x -W uid=<userName>
#
ldapsearch -xLLL -b "dc=blah,dc=com"
#
ldapsearch -x |grep dn
```
	4. Samba Authentication for LDAP users
		- **Install LDAP Authentication**
			- LDAP users be able to connect to samba and authenticate, we need these users to also show up in the system as "unix" users. One way to do this is to use libnss-ldap.
		```bash
sudo apt-get install libnss-ldapd
```
	There is no need to use the LDAP rootDN login credentials, so you can skip that step.
		* **Configure the LDAP profile for NSS:**
			- you will prompt to use configuration setup, if you make mistake use below command
```bash
sudo dpkg-reconfigure ldap-auth-config
```
		* **Restart the LDAP & Samba services:**
```bash
service slapd smbd nmbd restart
```
		* To quickly test the setup, see if getent can list the Samba groups
		```bash
		getent group
```

```bash
sudo apt-get install libnet-ssleay-perl
sudo apt-get install libcrypt-ssleay-perl
```
* result is new configure thge ldap profile for nss. configure the system to use ldap authentication
```bash
auth-client-config -t nss -p lac_ldap
pam-auth-update
```
* verify the loaded data has all the 'dn' values
  - take the backup of the newly loaded data
  - grep on the `dn: ` and save it to the new file for the newly loaded data and file used to upload the data respectively
  - use compare utility like `diff` or `sdiff` or `tkdiff` to compare these two files

### LDAP commands
* to take ldap data backup
```bash
slapd -l <backup_file_name>.ldiff
```
* write a shell script to take the backup
```bash
#!/bin/sh
LDAPBK=ldap-$( date +%y%m%d-%H%M ).ldiff
#BACKUPDIR=/tmp/ldap-bkup
BACKUPDIR=$(pwd)
#echo $BACKUPDIR
/usr/sbin/slapcat -v -b "dc=blah,dc=com" -l $BACKUPDIR/$LDAPBK
#gzip -9 $BACKUPDIR/$LDAPBK
```

* to create/add ldap data
```bash
ldapadd -c -x -D cn=admin,dc=blah,dc=com -W -f ldap-170731-1033.ldiff
```
* to modify
```bash
ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f ldap-170731-1033.ldiff
```

### Errors, Challanges Encountered
* **structuralObjectClass: no user modification allowed**
```bash
ldap_add: Constraint violation (19)
        additional info: structuralObjectClass: no user modification allowed
```
**Solution**: remove the `structuralObjectClass` line from the ldiff file 
* **how to add/delete/modify LDAP entries using ldiff file**
  - [Creating_Directory_Entries-LDIF_Update_Statements](https://access.redhat.com/documentation/en-US/Red_Hat_Directory_Server/8.2/html/Administration_Guide/Creating_Directory_Entries-LDIF_Update_Statements.html)
* **when ssh against the respective user, pemission denied error**
  - the LDAP base DN was not properly given
  - use authconfig tool to test the nss_ldap is enabed with proper settings, if server domain given: `blahblah.com` the LDAB base DN should be ` LDAP base DN = "dc=blahblah,dc=com"`
```bash
authconfig --test
# putput under nss_ldap from the above command:
nss_ldap is enabled
 LDAP+TLS is disabled
 LDAP server = "ldap://<ldap-server-ip>/"
 LDAP base DN = "dc=blahblah,dc=com"
```
* **Samba object class 'sambaSamAccount' requires attribute 'sambaSID'**
**Solution**:
Possix account should be added before it can be made available for samba server as the samba server uses its own hash to store the password
  - remove the samba attributes and add the user
  - modify the added user with the samba attributes
    - Refer this link to see the ldfif syntax/format for modification and use `ldapmodify` command to update the records: [Updating LDAP user information with Samba attributes](https://www.ibm.com/support/knowledgecenter/en/STXKQY_4.2.3/com.ibm.spectrum.scale.v4r23.doc/bl1adm_updateldapsmb.htm)
  - certain attributes needs to be deleted from the ldiff file like `entryUUID, creatorsName, createTimestamp, entryCSN, modifiersName, modifyTimestamp` and only sambaSamAccount objectClass to be added, following is the working sample:-
```bash
dn: uid=blah1,ou=People,dc=blah,dc=com
changetype: modify
add: objectClass
objectClass: sambaSamAccount
-
add: sambaLogonTime
sambaLogonTime: 0
-
add: sambaLogoffTime
sambaLogoffTime: 2147483647
-
add: sambaKickoffTime
sambaKickoffTime: 2147483647
-
add: sambaSID
sambaSID: <samba-id>
-
add: displayName
displayName:: IA==
-
add: cn
cn:: IA==
-
add: sambaAcctFlags
sambaAcctFlags: [U]
-
add: sambaNTPassword
sambaNTPassword: <passwd-hash>
-
add: sambaLMPassword
sambaLMPassword: <passwd-hash>
-
add: userPassword
userPassword:: <passwd-hash>
-
add: shadowLastChange
shadowLastChange: 16527
-
add: sambaPwdCanChange
sambaPwdCanChange: 2147483647
-
add: sambaPwdMustChange
sambaPwdMustChange: 2147483647
-
add: sambaPwdLastSet
sambaPwdLastSet: 1427981962
-
add: shadowMax
shadowMax: 99999
# this line should be blank here
dn: uid=blah2,ou=People,dc=blah,dc=com
changetype: modify
add: objectClass
objectClass: sambaSamAccount
-
.
.
.
```

## Ser1
### LDAP Verification
* 121 testing for authetication
```bash
authconf --test
```
- the LDAP base DN should be properly given:
  - use authconfig tool to test the nss_ldap is enabed with proper settings, if server domain given: `blahblah.com` the LDAB base DN should be ` LDAP base DN = "dc=blahblah,dc=com"`
```bash
authconfig --test
# putput under nss_ldap from the above command:
nss_ldap is enabled
 LDAP+TLS is disabled
 LDAP server = "ldap://<ldap-server-ip>/"
 LDAP base DN = "dc=blahblah,dc=com"
```

### Samba Server
**Samba authentication error**
* [troubleshotting samba mounting using LDAP authentication](https://forums.linuxmint.com/viewtopic.php?f=42&t=88146&start=0)
* [PAM, pam - Pluggable Authentication Modules for Linux](https://linux.die.net/man/8/pam)
```bash
[2017/08/04 09:46:31, 0] lib/smbldap.c:smbldap_connect_system(942)
ldap_connect_system: Failed to retrieve password from secrets.tdb
```
```bash
authconfig --smbservers=<sambaServerIP> --update
smbpasswd -W
smbtree
nmap -sS -sU -T4 <IP>
```
* Check and verify the cn is binding
	* In file: `/etc/samba/smb.conf`, `cn=root` was mentioned and when it was changed to `cn=admin`, it started working.
```bash
vi /etc/samba/smb.conf
ldap admin dn = cn=admin,dc=blah,dc=com
#ldap admin dn = cn=root,dc=blah,dc=com
```
