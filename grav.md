/*
Title: Grav
Decription: Grav
Author: Bhaskar Mangal
Date: 
Tags: Grav
*/

# Grav
* https://en.wikipedia.org/wiki/Semantic_URL#Slug
* https://getgrav.org


**Grav Installation**
* https://learn.getgrav.org/troubleshooting/permissions

```bash
ps aux | grep -v root | grep apache | cut -d\  -f1 | sort | uniq

#!/bin/sh
chown -R bhaskar:www-data .
find . -type f | xargs chmod 664
find ./bin -type f | xargs chmod 775
find . -type d | xargs chmod 775
find . -type d | xargs chmod +s
```

## Basics
https://www.tutorialspoint.com/grav/grav_dashboard.htm

### grav-creating-user-with-editor-role
http://blog.netgloo.com/2016/10/04/grav-creating-user-with-editor-role/

## Multisite setup
* https://learn.getgrav.org/advanced/multisite-setup
* https://github.com/getgrav/grav/issues/1501
* https://discourse.getgrav.org/t/multisite-setup-sub-directory/4674/9

 create sym links to maintain
 https://github.com/getgrav/grav/issues/1660

## Installed Plugins
### Admin
https://learn.getgrav.org/admin-panel/introduction

### Admin Addon - User Manager
https://github.com/david-szabo97/grav-plugin-admin-addon-user-manager
```
bin/gpm install admin-addon-user-manager
```

### login
https://github.com/getgrav/grav-plugin-login


### Git Sync
https://getgrav.org/blog/git-sync-plugin


## Errors
grav unable to create file /liscenses.yaml permission denied

### Multisite Quirks
**Admin Plugin**
- login screen after logout returns back to main website

`./plugins/admin/themes/grav/templates/partials/login.html.twig`

**Plugin Installation failed from admin panel**
https://github.com/getgrav/grav/issues/1215

`./plugins/admin/themes/grav/templates/partials/javascript-config.html.twig:5:`
`window.GravAdmin.config`


        <script type="text/javascript">
    window.GravAdmin = window.GravAdmin || {};
    window.GravAdmin.config = {
        current_url: '/~bhaskar/grav/admin/plugins/git-sync',
        base_url_relative: '/~bhaskar/grav/vidteq.com/admin',
        base_url_simple: '/~bhaskar/grav',
        route: 'git-sync',
        param_sep: ':',
                enable_auto_updates_check: '',
                admin_timeout: '1800',
        admin_nonce: 'b35bd0a0132f57c9cfd210747104c4c1',
        language: 'en',
        pro_enabled: '',
        notifications: 1,
        local_notifications: '',
        site: {
            delimiter: '==='
        }
    };
    window.GravAdmin.uri_params = {};

**git-sync, local setup issue**
https://stackoverflow.com/questions/42379684/gitlab-web-hook-requires-public-ip-in-url


## how-to-access-a-local-website-from-internet-with-port-forwarding

https://managewp.com/how-to-access-a-local-website-from-internet-with-port-forwarding

https://www.showip.net/?error=invalid+ip

You go into your router configuration and forward port 80 to the LAN IP of the computer running the web server.

Then anyone outside your network (but not you inside the network) can access your site using your WAN IP address (whatismyipcom).

You need to find the Access points ip, then try and log into it, then find anything that says DMZ and open that up, disable anything that protects against DMZ, once you have a DMZ open post the WAN or public IP address so we can help further. We need the WAN or Public IP address you have so we can help. Be sure to turn off the firewall and anything that could stop the DMZ.

https://www.youtube.com/watch?v=waTGCAgKIM0

Secure tunnels to localhost
”I want to expose a local server behind a NAT or firewall to the internet.”

https://ngrok.com/

https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html

https://vmokshagroup.com/blog/expose-your-localhost-to-web-in-50-seconds-using-ngrok/


https://stackoverflow.com/questions/23395129/how-does-ngrok-work-behind-a-firewall

https://developer.atlassian.com/blog/2015/05/secure-localhost-tunnels-with-ngrok/

ngrok http -auth "user:password" 3000


, http://127.0.0.1:4040. 

http://d8b374a2.ngrok.io 

http://d8b374a2.ngrok.io/~bhaskar/grav/vidteq.com/_bitbucket-git-sync

https://dashboard.ngrok.com/get-started

**git-sync multisite issue**
https://github.com/trilbymedia/grav-plugin-git-sync/issues/33

gitsync-uri

https://www.ubuntupit.com/install-various-desktop-environment-ubuntu/
https://www.linux.com/news/5-linux-desktop-environments-rise-2017
https://itsfoss.com/best-linux-desktop-environments/

./ngrok http -auth "user:bm20" 80



http://b77eb42d.ngrok.io/~bhaskar/grav/vidteq.com/_git-sync
http://localhost/~bhaskar/grav/vidteq.com/_git-sync
http://d8b374a2.ngrok.io/~bhaskar/grav/vidteq.com/_bitbucket-git-sync
