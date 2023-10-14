### this is an exploration of ttf to svg, and Open Brush draw.svg()

I used the following site to convert ttf to svg saved in [LUCON.svg](LUCON.svg)

https://convertio.co/ttf-svg/

I then parse the svg paths and send them to Open Brush via draw.svg()

![image](https://github.com/dwillington/open-brush/assets/8038214/3ce6b034-d71b-4f0a-bb20-a073cd9ba41d)

Unfortunately, they are not showing up correctly. Set aside the orientation or mirroring issues for now. It's seems 70-80% there. Look how _beautiful_ those curves look, omg the possiblities.

I tested the same svg path against an online visualizer and it shows up correctly.

https://svg-path-visualizer.netlify.app/

https://svg-path-visualizer.netlify.app/#M583%20-123v123q-162%200%20-367%2079v169q213%20-103%20367%20-103v537l-73%2048q-265%20178%20-265%20385q0%20149%2097%20250.5t253%20114.5v124h123v-124q148%20-9%20303%20-65v-162q-145%2072%20-303%2089v-529l67%20-40q274%20-161%20274%20-381q0%20-157%20-96%20-263.5t-257%20-128.5v-123h-123zM706%20148q173%2038%20173%20222%0Aq0%20119%20-128%20207l-45%2032v-461zM595%20891v440q-74%20-9%20-121%20-68t-47%20-142q0%20-108%20126%20-200z

M583 -123v123q-162 0 -367 79v169q213 -103 367 -103v537l-73 48q-265 178 -265 385q0 149 97 250.5t253 114.5v124h123v-124q148 -9 303 -65v-162q-145 72 -303 89v-529l67 -40q274 -161 274 -381q0 -157 -96 -263.5t-257 -128.5v-123h-123zM706 148q173 38 173 222
q0 119 -128 207l-45 32v-461zM595 891v440q-74 -9 -121 -68t-47 -142q0 -108 126 -200z

![image](https://github.com/dwillington/open-brush/assets/8038214/cb8f4d84-4b40-4237-b202-a1b7960cc74e)


There are _thousands_ of amazing fonts I think would be cool to bring into Open Brush. Eventually one could automate sizing / scaling, rotation, 3D block lettering, etc. (just some next step ideas)...

![image](https://github.com/dwillington/open-brush/assets/8038214/4d7ee655-e06f-4b6a-8117-0449bc7147ff)

