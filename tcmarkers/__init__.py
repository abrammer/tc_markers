__version__ = "0.0.2"

from .markers import NH_HU, NH_TS, SH_HU, SH_TS


HU = NH_HU
TS = NH_TS


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
        marks = ['o', SH_TS, SH_HU]
    else:
        marks = ['o', NH_TS, NH_HU]

    idx = bisect.bisect_right(limits, vmx)
    try:
        mark = marks[idx]
    except IndexError:
        raise ValueError("%d too high for dynamic marker choice x<500" % vmx)
    return mark
