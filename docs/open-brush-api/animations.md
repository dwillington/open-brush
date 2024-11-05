
Here is an "animation" in Open Brush using rapid swapping of layers to acheive a frame rate.

https://github.com/user-attachments/assets/de4b1d6b-228b-4b58-ac86-7861c3627b05

```
param_eq = {
  "name": "Riemann",
  "xformula": ["u*v"],
  "yformula": ["math.pow(v/t0,2)-math.pow(u/t0,2)"],
  "zformula": ["30*u"],
  "umin": ["-6"],"umax": ["6"],"vmin": ["-25"],"vmax": ["25"]
}
num_layers = 16
t = [i/(num_layers//2) + math.pi/2 for i in range(num_layers)]
```

It's a "Riemann" parameteric equation over time t0, a different layer sketched for each value in the list t above. NOTE: do not sketch on layer=0, only on layer>0. 
This is because the camera path "lives" in layer=0. Now, you can loop over swapping layers:

```
while True:
  for i in range(num_layers):
    num=i+1
    ob.layer.show(num)
    time.sleep(0.1)
    ob.layer.hide(num)
```

And while all this is occuring, you can create and record a camera path on the Main layer, which should be active as you never touched it programatically.

Note the final mp4 will have a stuttering effect, as it will capture moments when the canvas was blank while a layer was being swapped out, between hide and show.
You can remove these frames for a smooth mp4 as follows:

```
# deconstruct video to individual frames
ffmpeg -i $f -y -hide_banner %3d.png

# inspect the frames and file sizes to see a pattern in the blank canvas pngs, and set the threshold below, I used 100000

for file in *.png; do
  if [ $(stat -c%s "$file") -lt 100000 ]; then
    rm -rf "$file"
  fi
done

# reconstruct non blank canvas frames to mp4
ffmpeg -y -framerate 30 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p out.mp4</dev/null
```
