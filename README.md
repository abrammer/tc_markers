# TC Markers

This is a tiny repo that solely house Matplotib paths for Tropical Storm and Hurricane symbols unneccesarily duplicated for NH and SH direction.  

## What do the markers looks like:
Great Question, that's the most important thing right.  

<img src="./backend/TSmeta.svg">


## Usage:

matplotlib normalises marker size by their extent.  The TS and HU markers will therefore need to be 2x larger than a plain 'o' marker.  If someone knows a way round that I'd love for a plain 'o' marker to be the same relative size.  


```python
import matplotlib.pyplot as plt
import tcmarkers


fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(0.5, 0.5, marker=tcmarkers.HU, color='r', markeredgecolor='r', markersize=10)
ax.plot(0.25, 0.25, marker=tcmarkers.TS, color='r', markeredgecolor='r', markersize=10)

fig.show()
```

Dynamic selection of symbol
```python
import matplotlib.pyplot as plt
import tcmarkers


fig = plt.figure()
ax = fig.add_subplot(111)

for i, vmax in enumerate([33, 34, 64,]):
    ax.plot(i, 2, marker=tcmarkers.tc_marker(vmax), color='r', markeredgecolor='r', markersize=10)
    # pass latitude and SH storms returned for lat < 0
    ax.plot(i, 1, marker=tcmarkers.tc_marker(vmax, -30), color='r', markeredgecolor='r', markersize=10)

fig.show()
```
Only 4 markers are available, `NH_TS, NH_HU, SH_TS, SH_HU` alias of `TS` and `HU` for quick use of the most common.


## Contributing:
Have a better TC Marker? Update the SVG using the 5 characters IDs above for each object. The current markers are not perfect but I don't know how to inkscape well.  Run the backend script to regenerate the `markers.py` file and submit a PR.  


