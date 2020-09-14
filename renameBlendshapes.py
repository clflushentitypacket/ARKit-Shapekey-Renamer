import bpy

# get the selected object
selected_object = bpy.context.object

# get its shapekeys
shape_keys = selected_object.data.shape_keys.key_blocks

exceptions = ["mouthLeft", "mouthRight", "jawLeft", "jawRight"]

for key in shape_keys:
    if key.name not in exceptions:
        key.name = key.name.replace("Right", "_R")
        key.name = key.name.replace("Left", "_L")
