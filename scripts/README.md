## Open Brush API Usage via JavaScript

Here I maintain my modifications to the original Open Brush [exampleScripts](http://localhost:40074/exampleScripts).
Some HTML requires to be served up via a web server in which case I run the following in this scripts folder:
python3 -m http.server 8000

http://localhost:8000/generative_art.html
-------------
<img src="images/piet_mondrian_UNLITHULL.JPG" width="400" /> <img src="images/triangular_mesh.JPG" width="400" />
<img src="images/hypnotic_squares.JPG" width="400" /> <img src="images/tiled_lines.JPG" width="400" />
<img src="images/CubicDisarray.JPG" width="400" /> <img src="images/JoyDivision.JPG" width="400" />

http://localhost:8000/image_art.html
-------------
Original  | image_art.html -> Open Brush
------------- | -------------
![img](images/gundam.jpg) | ![img](images/gundam_ascii.jpg)

http://localhost:8000/lindenmayer.html
-------------
<img src="images/penrose_tiles.JPG" width="600" />




Use Configuration
-------------
https://docs.openbrush.app/user-guide/open-brush-api#how-do-i-configure-it