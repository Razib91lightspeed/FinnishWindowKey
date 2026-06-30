# Finnish Window Key L-Shape

A simple FreeCAD model for a Finnish-style L-shaped window key.

## Dimensions

- Long arm: 90 mm
- Short arm: 50 mm
- Square profile: 7 mm × 7 mm
- Joint: rounded L-corner
- Shape: plain L-shape, no extra triangular support, so the long side can still fit into the window mechanism

## FreeCAD

Open FreeCAD and run the Python script in the FreeCAD Python console or as a macro.

Main parameters in the script:

```python
profile = 7
height = 7
long_arm = 90
short_arm = 50
joint_radius = 3.0
```

You can adjust `long_arm` and `short_arm` if another size is needed.

## 3D Printing Settings

Recommended settings for strength:

- Material: PETG or ASA
- Wall loops / perimeters: 6–8
- Infill: 100%
- Top layers: 6–8
- Bottom layers: 6–8
- Layer height: 0.16–0.20 mm
- Print orientation: flat on the bed

## Strength Note

The model should stay solid in FreeCAD. Extra strength should mainly come from slicer settings such as more wall loops, high infill, and strong material.
