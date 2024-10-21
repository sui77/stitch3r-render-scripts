import bpy
import os

# ======== install stitch3r + load file =============
addon_file_path=os.getcwd()+'/stitch3r_v2.zip'
bpy.ops.preferences.addon_install(overwrite=True, target='DEFAULT', filepath=addon_file_path)
bpy.ops.preferences.addon_enable(module = 'stitch3r_v2')
