## Open Brush API Usage via Python

Programmatic use of API via Python. Guess I'm learning Python ha.

```
# export OB_HOST=192.168.86.55 # IP of OB in OCULUS

source ~/venv_3.8/bin/activate

# directly from bash
sendcom new
sendcom viewonly.toggle
sendcom user.move.to=0,0,10


#sendcom environment.type=Passthrough
#sendcom environment.type=Standard

```

python3 image_art.py drawMindMap
-------------
<img src="images/mindmap.JPG" width="400" />

python3 image_art.py drawRandomPath
-------------
<img src="images/random_path.JPG" width="400" /> | <img src="images/random_path_2.JPG" width="400" />

