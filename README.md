# stitch3r-render-scripts

### step 1
Put these files into the same directory on the remote machine
- init.py
- settings.py
- [stitch3r_v2.zip](https://blendermarket.com/products/stitch3r)
- your YourBlenderFile.blend file

### step 2
Edit output and render settings in settings.py (e.g. to make a low resolution, couple frames test run)

### step 3
Start rendering with

    blender -P init.py YourBlenderFile.blend -P settings.py -a

(-P loads a python script, -a starts rendering animation)
