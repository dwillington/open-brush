# docs


### api bindings for python

https://gist.github.com/andybak/c700120232ca68a90adc791f75c8a16c

```
unlink ~/venv_3.8/lib/python3.8/site-packages/ob.py
#ln -s /root/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3.8/lib/python3.8/site-packages/ob.py
ln -s /mnt/c/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3/lib/python3.10/site-packages/ob.py

ipython
from ob import ob

ob.new()
ob.viewonly.toggle()


```

### Camera Drift

Reproducing the problem:

1. Launch Open Brush
2. Stand on a spot you’ve marked (or chosen) on the real-world floor and look towards a fixed point on the wall facing you.
3. In VR - draw a circle around you at waist height and then draw a line pointing forwards in the direction you are facing to mark your current "forwards" direction.

At this point:
1. take the headset off
2. press the power button to send it into sleep mode
3. put the headset back
4. press "power" to wake the headset.

Observation: You will now most likely be out of alignment with the marks you drew previously.

The headset doesn’t always place you in the same position in the virtual world that it previously used when it awakes from sleep mode.
 
Solution:

Every time the headset is woken from sleep mode you’ll need to set the direction. Ensure you are in the same spot and facing the same direction and then long-press the Oculus button.

To demonstrate this solves the problem demonstrated above you can follow these steps:

1. Launch Open Brush
2. Same as before - stand on a marked spot and look at a fixed "forward" point.
3. Keeping your gaze at the point on the wall, long press the Oculus button on my right controller.
4. Draw the circle and forward marker as before.

Remove the headset, put it to sleep then awaken it, you can always bring the world back into alignment as long as you look at the point on the wall and long-press the Oculus button.

Note: this is only necessary if the headset has gone into sleep mode. An alternative is to change the system settings so that it doesn't go to sleep so quickly. You can also place a piece of tape over the proximity sensor so it thinks the headset is always being worn.

https://levelup.gitconnected.com/how-to-keep-your-oculus-quest-2-from-going-to-sleep-when-you-take-it-off-8cfb4b661248

(The only thing that might cause the headset to lose its position is if you cover up enough of the external cameras to confuse the tracking. This is fairly hard to do by accident but do some testing on your end to confirm the above is an effective solution)


Moving forward...

There's some new Quest SDK Platform features that point to a different approach. Have a play with ShapesXR - especially the 1:1 mode in passthrough. 

https://www.shapesxr.com/post/update-1-1-mode-real-world-reference-passthrough-material-teleportation-tool

Update - 1:1 mode, Real-world reference, Passthrough material, Tele...

Over the past months, we have worked hard with many of our users to test and improve SIGNIFICANTLY the passthrough feature and we are glad to release so many functionalities that will unlock incredible opportunities for designing and prototyping immersive apps as well as design and mockup products or experiences on top of the physical world.

Update - 1:1 mode, Real-world reference, Passthrough material, Tele...

I wonder if simply adding a desk or other furniture to the Quest room setup will force it be more consistent in it's alignment. Hard to see how the new mixed reality features would work properly otherwise

The manual solution is just a "calibrate to room" feature that gets you to place the controllers on a memorized spot and uses that to re-align. 
