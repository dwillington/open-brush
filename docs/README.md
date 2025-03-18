# docs


### api bindings for python

A lot of my code depends on the bindings file being available in your python environment.
For e.g. I may have a venv_3.8. I have to place the [ob.py](https://github.com/dwillington/open-brush/blob/main/docs/api_bindings/ob.py) file there.

```
unlink ~/venv_3.8/lib/python3.8/site-packages/ob.py
#ln -s /root/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3.8/lib/python3.8/site-packages/ob.py
ln -s /mnt/c/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3/lib/python3.10/site-packages/ob.py

ipython
from ob import ob

ob.new()
ob.viewonly.toggle()


```

Original: https://gist.github.com/andybak/c700120232ca68a90adc791f75c8a16c

### How to hide the guardian on Quest headsets

https://deovr.com/blog/156-guide-how-to-hide-the-guardian-on-quest-headsets-for-deovr

```
Download Platform Tools 
Extract the archive
Open the extracted folder
Type into folder path (C:\%your_path%\platform-tools) the command "cmd" (without quotes) and press "Enter"
Connect the headset to the PC via cable
Turn on the headset
On the PC, paste the command adb shell setprop debug.oculus.guardian_pause 1 into the pop-up terminal from step #4 and press "Enter";
The command for disabling is "adb shell setprop debug.oculus.guardian_pause 1"
The command for enabling is "adb shell setprop debug.oculus.guardian_pause 0"
```

This worked...

![image](https://github.com/user-attachments/assets/31d014b4-439f-474a-8138-3b330fc51454)
