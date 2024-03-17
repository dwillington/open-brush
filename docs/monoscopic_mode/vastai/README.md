##### Using vastai platform to remotely access gpu based desktop for running Open Brush Monoscopic

Allows for testing 3D generations via Open Brush API in Monoscopic Mode before moving to Open Brush VR.

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
# screen-fullscreen 0 OPTION IS USEFUL IN ALLOWING YOU TO ACCESS OS CONTROLS
chmod a+x /opt/StandaloneLinux64-Monoscopic/OpenBrush-tempprexr2_Data screen-fullscreen 0
````

![image](https://github.com/dwillington/open-brush/assets/8038214/8b6ad107-bad4-4e8f-88b6-01d322554bab)

By now you should have the option to "OPEN" the Desktop experience via browser. This can take 2-3 minutes to become available from initial instance creation, so be patient.

![image](https://github.com/dwillington/open-brush/assets/8038214/e6e68fdc-02a2-4ea3-842b-7d3510e0ba61)

1) Open Konsole Terminal and run "./OpenBrush-tempprexr2_Data" from "/opt/StandaloneLinux64-Monoscopic"

![image](https://github.com/dwillington/open-brush/assets/8038214/833f3f52-0aeb-44ac-b630-e63b8ef0db6b)

```
# SEND SOME TEST COMMANDS
cd ~/
git clone https://github.com/dwillington/open-brush.git
# SHELL SCRIPT TO SEND API COMMANDS TO MONOSCOPIC FROM SHELL
/bin/cp -r open-brush/bash/ob.sh /usr/local/bin/ob
ob new
ob user.move.to=-10,10,20
ob draw.text=hello
ob viewonly.toggle
```

![image](https://github.com/dwillington/open-brush/assets/8038214/14e62b80-3154-4ded-b86a-9dd3d5a64870)

If all goes well, it shoudl look like this...

![image](https://github.com/dwillington/open-brush/assets/8038214/ff1def40-868b-4329-a3ed-3b4877ad6c70)

Don't forget to visit the help page...

![image](https://github.com/dwillington/open-brush/assets/8038214/83e33dad-a714-466e-8b9f-7dae2be35f01)




To run some Python scripts in this repo...

```
apt install virtualenv -y
virtualenv -p python3 ~/venv_3
source ~/venv_3/bin/activate
cd ~/open-brush/python_scripts
pip install -r requirements.txt
cd ~/open-brush/python_scripts/geoDome
python geoDome.py
```


![image](https://github.com/dwillington/open-brush/assets/8038214/f5ef77cf-1701-45bd-bb2b-2d233d8cd6fe)
