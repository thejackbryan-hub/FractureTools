"""
Single Edge Through Crack Geometry

Reference
---------
MechaniCalc Stress Intensity Factor Solutions

Returns geometry correction factors only.
"""

from math import cos, pi, sin, sqrt, tan


def single_edge_through_crack(
    a: float,
    b: float,
) -> tuple[float, float]:
    """
    Calculate geometry correction factors for a single edge
    through crack in a finite-width plate.

    Parameters
    ----------
    a : float
        Crack length.

    b : float
        Plate width.

    Returns
    -------
    tuple
        (Yt, Yb)
    """

    alpha = a / b

    Yt = (
        0.265 * (1.0 - alpha) ** 4
        + (0.857 + 0.265 * alpha)
        / (1.0 - alpha) ** 1.5
    )

    Yb = (
        sqrt(
            (2.0 / (pi * alpha))
            * tan(pi * alpha / 2.0)
        )
        * (
            (
                0.923
                + 0.199
                * (1.0 - sin(pi * alpha / 2.0)) ** 4
            )
            / cos(pi * alpha / 2.0)
        )
    )

    return Yt, Yb

def edge_curve(points: int = 500):
    """
    Generate the geometry factor curve for plotting.
    """

    import numpy as np

    x = np.linspace(0.001, 0.95, points)

    y = (
        0.265 * (1.0 - x) ** 4
        + (0.857 + 0.265 * x)
        / (1.0 - x) ** 1.5
    )

    return x, y

