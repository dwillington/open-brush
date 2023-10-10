### How to setup monoscopic on a remote windows instance (i.e. no local gpu)

https://cloud.google.com/compute/docs/connect/windows-ssh

https://jmmv.dev/2022/02/wsl-ssh-access.html

https://stackoverflow.com/questions/16212816/setting-up-openssh-for-windows-using-public-key-authentication

add your id_rsa.pub to c:\Users\root\.ssh\authorized_keys

https://github.com/git-for-windows/build-extra/releases

setup the above to support rsync:

rsync -chavzP --rsync-path='/git-sdk-64/usr/bin/rsync.exe' --exclude '.git' --exclude '.gitignore' \
  /mnt/c/temp/git_repos/dwillington/open_brush \
  user@host:/c/temp/git_repos/dwillington



https://medium.com/analytics-vidhya/how-to-auto-shutdown-an-idle-vm-instance-on-gcp-to-cut-fat-bills-b08ae20437af

```
nohup /mnt/c/Users/root/idle-shutdown.sh &> /tmp/idle-shutdown.log
gcloud compute instances stop ...
```


