from pathlib import Path
from matplotlib.testing import compare, exceptions
import matplotlib.pyplot as plt
import tcmarkers


def test_plotting():
    expectedimg = Path(__file__).resolve().parent / 'expected.png'
    fig = plt.figure()
    ax = fig.add_subplot(111)

    kwargs = {'markersize': 25, 'color':'r', 'markeredgecolor':'r'}
    ax.plot(0.3, 0.25, marker=tcmarkers.HU, **kwargs)
    ax.plot(0.3, 0.20, marker=tcmarkers.SH_HU, **kwargs)
    ax.plot(0.25, 0.25, marker=tcmarkers.TS,**kwargs)
    ax.plot(0.25, 0.20, marker=tcmarkers.SH_TS, **kwargs)
    ax.plot(0.20, 0.25, marker=tcmarkers.TD, **kwargs)
    ax.plot(0.20, 0.20, marker=tcmarkers.TD, **kwargs)

    ax.set_xlim(0.15, 0.35)
    ax.set_ylim(0.15, 0.30)
    fig.savefig('result.png')
    result =  compare.compare_images('result.png', expectedimg, 0.001)
    if result is not None:
        print(result)
        raise exceptions.ImageComparisonFailure

if __name__ == "__main__":
    test_plotting()