import nuke

nuke.knobDefault("Tracker4.label", "[value reference_frame]")

import GrayAutoBackdrop
nuke.menu('Nuke').addCommand('Extra/Gray Auto Backdrop', lambda: GrayAutoBackdrop.GrayAutoBackdrop(), "shift+b", shortcutContext=2)

import readWrite


nuke.menu("Nuke").addCommand("Utilities/Creat read from Write", "readWrite.readWrite()", "ctrl+r")


nuke.knobDefault('Roto.cliptype','no clip')
nuke.knobDefault('Merge2.label','[value bbox]')
nuke.knobDefault('Merge2.label','[value mix]')
nuke.knobDefault('Shuffle2.label','[value in1]')
nuke.knobDefault('Shuffle.label','[value in]')
nuke.knobDefault('Switch.label','[value which]')
nuke.knobDefault("Merge2.bbox", "B")


nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox union", False)', "shift+r", shortcutContext=2) 
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox union", False)', "shift+g", shortcutContext=2) 
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Max', 'nuke.createNode("Merge2", "operation max bbox union", False)', "shift+t", shortcutContext=2) 
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Plus', 'nuke.createNode("Merge2", "operation plus bbox union", False)', "shift+y", shortcutContext=2) 
nuke.menu('Nodes').addMenu('Shuffle/Shuffles').addCommand('Shuffle', 'nuke.createNode("Shuffle2")', "shift+e", shortcutContext=2)
 
 
 
# ----- TOGGLE TRACKER AND MERGE OPERATIONS ----------------------- 
# -- Inverse any merge or match move node with ctrl+shift+z ie under/over ie stabilize/matchmove 
 
def operationSwitcher(): 
    node = nuke.selectedNode() 
    merge_ops = {'stencil': 'mask', 'over': 'under', 'from': 'plus', 'out': 'in'} 
    if node.Class() == "Merge2": 
        current_op = node['operation'].value() 
        if current_op in merge_ops.keys(): 
            node['operation'].setValue(merge_ops[current_op]) 
        elif current_op in merge_ops.values(): 
            # Create reverse dictionary
            reverse_ops = {v: k for k, v in merge_ops.items()}
            node['operation'].setValue(reverse_ops[current_op]) 
 
 
# Add to edit menu 
nuke.menu('Nuke').addCommand('Edit/Switch Operation', operationSwitcher, "ctrl+shift+z")




