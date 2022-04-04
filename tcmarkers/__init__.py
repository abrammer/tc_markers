__version__ = "0.0.3"

import numpy as np
from matplotlib import transforms
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

from .markers import EX_path, NH_HU_path, NH_TS_path, TD_path

_MARKERSCALE = np.max(np.abs(NH_HU_path.vertices))


class TCMarkerStyle(MarkerStyle):
    def _set_custom_marker(self, path):
        self._transform = Affine2D().scale(1. / _MARKERSCALE)
        self._path = path


NH_HU = HU = TCMarkerStyle(NH_HU_path)
NH_TS = TS = TCMarkerStyle(NH_TS_path)
SH_TS = TCMarkerStyle(NH_TS_path.transformed(transforms.Affine2D().scale(-1, 1)))
SH_HU = TCMarkerStyle(NH_HU_path.transformed(transforms.Affine2D().scale(-1, 1)))

HU = NH_HU
TS = NH_TS

TD = TCMarkerStyle(TD_path)
NH_TD = TD
SH_TD = TD

EX = TCMarkerStyle(EX_path)
NH_EX = EX
SH_EX = EX


def tc_marker(vmx, lat=5):
    """ Returns marker for given intensity and latitude

    Parameters
    ----------
    vmx : num
        Intensity of storm in kts
    lat : num, optional
        latitude of storm (to decide on SH orientation), by default 5

    Returns
    -------
    matplotlib.path.Path or str
        custom Path for TS or HU strength, or plain 'o' for <= 33 kt

    Raises
    ------
    ValueError
        if vmx is too great (< 500 kts), raise error as something is wrong
    """
    import bisect
    limits = [34, 64, 500]
    if lat < 0:
        marks = [TD, SH_TS, SH_HU]
    else:
        marks = [TD, NH_TS, NH_HU]

    idx = bisect.bisect_right(limits, vmx)
    try:
        mark = marks[idx]
    except IndexError:
        raise ValueError("%d too high for dynamic marker choice x<500" % vmx)
    return mark
