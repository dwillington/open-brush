Original Source: https://github.com/JakobGlock/Generative-Art

```
source ~/venv_3.6.8/bin/activate
# IF NOT LOCALHOST
export OB_HOST="10.0.2.2"
```

python3 Line_Grid.py
-------------
<img src="images/Line_Grid.JPG" width="400" /> | <img src="images/Line_Grid_2.JPG" width="400" />

python3 Parallel_Lines.py
-------------
<img src="images/Parallel_Lines.JPG" width="400" /> | <img src="images/Parallel_Lines_2.JPG" width="400" />

python3 Circular.py
-------------
<img src="images/Circular.JPG" width="400" /> | <img src="images/Circular_2.JPG" width="400" />

python3 Line_Walker.py
-------------
<img src="images/Line_Walker.JPG" width="400" />  | <img src="images/Line_Walker_2.JPG" width="400" />  

python3 Mosaic_Circles.py
-------------
<img src="images/Mosaic_Circles.JPG" width="400" /> | <img src="images/Mosaic_Circles_JoinMinusOne.JPG" width="400" />  

python3 Offset_Quads.py
-------------
<img src="images/Offset_Quads.JPG" width="400" /> | <img src="images/Offset_Quads_2.JPG" width="400" />

python3 Masonry.py
-------------
<img src="images/Masonry.JPG" width="400" /> | <img src="images/Masonry_2.JPG" width="400" />

python3 Perlin_Brush_Stroke.py
-------------
<img src="images/Perlin_Brush_Stroke.JPG" width="400" /> | <img src="images/Perlin_Brush_Stroke_2.JPG" width="400" />


```
"Line_Walker"
# takes long, do on its own, speed up
"Masonry"
"Offset_Quads" 

python3 Line_Grid.py
python3 Mosaic_Circles.py
python3 Parallel_Lines.py
python3 Circular.py
python3 Magnetic_Flow.py
python3 Masonry.py
python3 Offset_Quads.py

declare -a arr=("Line_Grid" "Mosaic_Circles" "Parallel_Lines" "Perlin_Brush_Stroke" "Circular" "Magnetic_Flow" )
for i in "${arr[@]}"
do
  python3 ${i}.py
  sleep 5
done

```