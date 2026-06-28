"""
Center Through Crack Geometry

Reference
---------
MechaniCalc Stress Intensity Factor Solutions

Returns geometry correction factors only.
"""

from math import cos, pi, sqrt


def sec(x: float) -> float:
    """
    Return the secant of an angle in radians.
    """
    return 1.0 / cos(x)


def center_through_crack(
    a: float,
    b: float,
) -> tuple[float, float]:
    """
    Calculate geometry correction factors for a center through crack
    in a finite-width plate.

    Parameters
    ----------
    a : float
        Crack half-length.

    b : float
        Plate half-width.

    Returns
    -------
    tuple
        (Yt, Yb)
    """

    ratio = a / b

    Yt = sqrt(sec(pi * ratio / 2.0))

    Yb = Yt / 2.0

    return Yt, Yb

def center_curve(points: int = 500):
    """
    Generate the geometry factor curve for plotting.
    """

    import numpy as np

    x = np.linspace(0.001, 0.95, points)

    y = np.sqrt(
        1.0 / np.cos(np.pi * x / 2.0)
    )

    return x, y
