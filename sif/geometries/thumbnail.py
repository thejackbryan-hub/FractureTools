"""
Thumbnail Crack in a Solid Cylinder Geometry

Reference
---------
MechaniCalc Stress Intensity Factor Solutions

Returns geometry correction factors only.
"""

from math import cos, pi, sin, sqrt, tan


def sec(x: float) -> float:
    """
    Return sec(x) where x is in radians.
    """
    return 1.0 / cos(x)


def thumbnail_crack(
    a: float,
    diameter: float,
) -> tuple[float, float]:
    """
    Calculate geometry correction factors for a thumbnail
    crack in a solid cylinder.

    Parameters
    ----------
    a : float
        Crack depth.

    diameter : float
        Cylinder diameter.

    Returns
    -------
    tuple
        (Yt, Yb)
    """

    beta = pi * a / (2.0 * diameter)

    G = (
        0.92
        * (2.0 / pi)
        * sec(beta)
        * sqrt(tan(beta) / beta)
    )

    H = 1.0 - sin(beta)

    Yt = G * (
        0.752
        + 1.286 * beta
        + 0.370 * H**3
    )

    Yb = G * (
        0.923
        + 0.199 * H**4
    )

    return Yt, Yb

def thumbnail_curve(
    diameter: float,
    points: int = 500,
):
    """
    Generate the geometry factor curve for a thumbnail crack
    in a solid cylinder.

    Parameters
    ----------
    diameter : float
        Cylinder diameter.

    points : int
        Number of points used for the curve.

    Returns
    -------
    tuple
        (a_over_D, Yt)
    """

    import numpy as np

    a_over_D = np.linspace(0.001, 0.95, points)

    Yt = np.zeros(points)

    for i, ratio in enumerate(a_over_D):

        a = ratio * diameter

        Yt[i], _ = thumbnail_crack(
            a,
            diameter,
        )

    return a_over_D, Yt