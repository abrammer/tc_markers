# TC Markers

This is a tiny repo that solely houses Matplotib paths for Tropical Storm and Hurricane symbols, neccesarily duplicated for NH and SH direction.  

## What do the markers look like:
Great question, that's the most important thing right. Here's the current view of them:

<img src="https://github.com/abrammer/tc_markers/raw/main/backend/TSmeta.svg" alt="See repo for SVG of markers">


## Usage:

Version 0.0.3 includes a TD and EX symbol which will be the correct size for TS and HU comparison. 


```python
import matplotlib.pyplot as plt
import tcmarkers


fig = plt.figure()
ax = fig.add_subplot(111)
marker_kwargs = {'markersize': 25, 'color':'r', 'markeredgecolor':'r'}
ax.plot(0.35, 0.25, marker=tcmarkers.EX, **marker_kwargs)
ax.plot(0.35, 0.20, marker=tcmarkers.SH_EX, **marker_kwargs)
ax.plot(0.3, 0.25, marker=tcmarkers.HU, **marker_kwargs)
ax.plot(0.3, 0.20, marker=tcmarkers.SH_HU, **marker_kwargs)
ax.plot(0.25, 0.25, marker=tcmarkers.TS,**marker_kwargs)
ax.plot(0.25, 0.20, marker=tcmarkers.SH_TS, **marker_kwargs)
ax.plot(0.20, 0.25, marker=tcmarkers.TD, **marker_kwargs)
ax.plot(0.20, 0.20, marker=tcmarkers.SH_TD, **marker_kwargs)
fig.show()
```

<img src="https://github.com/abrammer/tc_markers/blob/main/tests/expected.png?raw=true" alt="See repo for SVG of markers">


Dynamic selection of symbol based on vmax.  Function based on string type coming next.

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
4 markers are now available, `TD`, `TS`, `HU` and `EX` these are available rotated for SH or original NH as well with the `NH_` or `SH_` prefix. e.g. `NH_TD`, `NH_TS`, `NH_HU`,`NH_EX`, `SH_TD`, `SH_TS`, `SH_HU`, `SH_EX`.


## Contributing:
Have a better TC Marker? Update the SVG using the 4 characters IDs above for each object. The current markers are not perfect but I don't know how to inkscape well.  Run the backend script to regenerate the `markers.py` file and submit a PR.  


## Future:
Maybe creating a child class of the matplotlib.path.Path would be nice. This could include a nicer __repr__ and a name attribute, allowing the user to check which marker came back from the selection function?