### bash scripts run on MSYS2 on Windows or CentOS 7 on VirtualBox

```
/bin/cp -r ob.sh /usr/local/bin/ob

# SAMPLE ob COMMANDS FROM THE SHELL TO MONOSCOPIC APPLICATION
ob new
ob user.move.to=-10,10,20
ob draw.text=hello
ob viewonly.toggle

ob brush.size.set=0.1
ob brush.type=Icing
ob draw.polygon=6,1,0

```

[jpg_to_ob.sh](jpg_to_ob.sh) script orchestrates the conversion of 1-N JPGs in to Brush Stroke Images in Open Brush. "Listening" for the API command debug.brush (in %USERNAME%/AppData/LocalLow/Icosa/Open Brush/Player.log) is used as a kind of [Sentinel Value](https://en.wikipedia.org/wiki/Sentinel_value) to indicate that Open Brush has finished creating the image.

[https://docs.openbrush.app/user-guide/open-brush-api](https://docs.openbrush.app/user-guide/open-brush-api)






