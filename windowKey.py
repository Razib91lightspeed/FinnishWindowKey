import FreeCAD as App
import FreeCADGui as Gui
import Part

# New document
doc = App.newDocument("Finnish_Window_Key_L_90x50_Rounded")

# Dimensions in mm
profile = 7        # square stick: 7mm x 7mm
height = 7

long_arm = 90      # long side
short_arm = 50     # short side

# Rounded joint only
joint_radius = 3.0

# Create two straight arms
horizontal = Part.makeBox(long_arm, profile, height)
vertical = Part.makeBox(profile, short_arm, height)

# Fuse into one solid L shape
l_shape = horizontal.fuse(vertical).removeSplitter()

# Round only the L joint vertical edges
fillet_edges = []

for edge in l_shape.Edges:
    bb = edge.BoundBox
    center = edge.CenterOfMass

    is_vertical = (
        bb.ZLength > 6.5 and
        bb.XLength < 0.01 and
        bb.YLength < 0.01
    )

    if is_vertical:
        x = round(center.x, 3)
        y = round(center.y, 3)

        # Outside corner of L
        if abs(x - 0) < 0.01 and abs(y - 0) < 0.01:
            fillet_edges.append(edge)

        # Inside corner of L
        if abs(x - profile) < 0.01 and abs(y - profile) < 0.01:
            fillet_edges.append(edge)

# Apply rounded joint
if fillet_edges:
    l_shape = l_shape.makeFillet(joint_radius, fillet_edges)

# Center object around origin
l_shape.translate(App.Vector(-long_arm / 2, -short_arm / 2, -height / 2))

# Add to document
obj = doc.addObject("Part::Feature", "Finnish_Window_Key_90x50_7mm_Rounded")
obj.Shape = l_shape

doc.recompute()

# View
Gui.SendMsgToActiveView("ViewFit")
Gui.ActiveDocument.ActiveView.viewIsometric()

print("Created Finnish window key: 90mm x 50mm, 7x7mm profile, rounded L joint.")
