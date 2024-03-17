
https://cloud.vast.ai/templates/
1) Click Templates on Left
2) Search "Desktop"
3) Click EDIT on "GLX Desktop"

![image](https://github.com/dwillington/open-brush/assets/8038214/9727e1f6-26ee-417e-8eac-0b1b83b7451b)

1) Under Docker Options, expose a couple extra ports: -p 8081:8081 -p 8082:8082
2) Enable "Run interactive shell server" for SSH access, very important.
3) Click "Select and Save" at the bottom

![image](https://github.com/dwillington/open-brush/assets/8038214/76ec43ff-cc0c-4a4d-b9c6-dad98ad0f6b2)

1) I choose "Unverified Machines" (bottom left), otherwise I have limited expensive options
2) Choose your GPU from the drop down, 3060 should be enough and it's cheap
3) Click Rent

![image](https://github.com/dwillington/open-brush/assets/8038214/e62ea3e3-fdb3-40de-88b7-16d3479962c1)

1) Go to Instances
2) Click Shell Icon
3) Copy "Direct ssh connect" string

![image](https://github.com/dwillington/open-brush/assets/8038214/f0fb19e3-ec5e-49c9-81c0-82f7f42b28a6)


```
# PASTE "Direct ssh connect" string INTO ssh_url VAR BELOW
ssh_url="ssh -p 26065 root@27.65.59.89 -L 8080:localhost:8080"
IFS=' ' read -ra ADDR <<< "$ssh_url"
ssh_port=${ADDR[2]} # PARSE OUT PORT 26065 FROM ssh_url
ssh_ip=${ADDR[3]} # PARSE OUT root@27.65.59.89 FROM ssh_url
$ssh_url # RUN SSH COMMAND TO CONNECT
```

![image](https://github.com/dwillington/open-brush/assets/8038214/82b297b7-9338-43b9-9a37-13319fb301f4)


```
# SETUP LINUX MONOSCOPIC
wget http://wearcam.org/abaq/openbrush/Linux%20Monoscopic%20Experimental.zip
unzip 'Linux Monoscopic Experimental.zip' > /dev/null 2>&1
mv StandaloneLinux64-Monoscopic/ /opt
chmod a+x /opt/StandaloneLinux64-Monoscopic/OpenBrush-tempprexr2_Data
````

![image](https://github.com/dwillington/open-brush/assets/8038214/8b6ad107-bad4-4e8f-88b6-01d322554bab)
