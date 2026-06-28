"""
Corner Surface Crack Geometry

Reference
---------
MechaniCalc Stress Intensity Factor Solutions

Returns geometry correction factors only.
"""

from math import cos, pi, sin, sqrt


def sec(x: float) -> float:
    """Return sec(x) where x is in radians."""
    return 1.0 / cos(x)


def corner_surface_crack(
    a: float,
    c: float,
    b: float,
    t: float,
    phi: float,
) -> tuple[float, float]:
    """
    Calculate geometry correction factors for a corner
    surface crack.

    Parameters
    ----------
    a : float
        Crack depth.

    c : float
        Crack half-length.

    b : float
        Plate half-width.

    t : float
        Plate thickness.

    phi : float
        Crack front angle (radians).

    Returns
    -------
    tuple
        (Yt, Yb)
    """

    if a <= c:

        Q = 1.0 + 1.464 * (a / c) ** 1.65

        f_phi = (
            (a / c) ** 2 * cos(phi) ** 2
            + sin(phi) ** 2
        ) ** 0.25

        f_w = sqrt(
            sec(
                (pi * c / (2.0 * b))
                * sqrt(a / t)
            )
        )

        M1 = 1.08 - 0.03 * (a / c)

        M2 = -0.44 + 1.06 / (0.30 + a / c)

        M3 = (
            -0.50
            - 0.25 * (a / c)
            + 14.8 * (1.0 - a / c) ** 15
        )

        g1 = (
            1.0
            + (
                0.08
                + 0.40 * (a / t) ** 2
            )
            * (1.0 - sin(phi)) ** 3
        )

        g2 = (
            1.0
            + (
                0.08
                + 0.15 * (a / t) ** 2
            )
            * (1.0 - cos(phi)) ** 3
        )

        F = (
            (
                M1
                + M2 * (a / t) ** 2
                + M3 * (a / t) ** 4
            )
            * f_phi
            * f_w
            * g1
            * g2
        )

    else:

        Q = 1.0 + 1.464 * (c / a) ** 1.65

        f_phi = (
            (c / a) ** 2 * sin(phi) ** 2
            + cos(phi) ** 2
        ) ** 0.25

        f_w = sqrt(
            sec(
                (pi * c / (2.0 * b))
                * sqrt(a / t)
            )
        )

        #
        # Same branch used in your MATLAB version.
        #
        F = f_phi * f_w

    Y = F / sqrt(Q)

    return Y, Y

def corner_curve(
    a: float,
    c: float,
    b: float,
    t: float,
    points: int = 181,
):
    """
    Generate the geometry factor curve versus crack-front angle.

    Parameters
    ----------
    a : float
        Crack depth.

    c : float
        Crack half-length.

    b : float
        Plate half-width.

    t : float
        Plate thickness.

    points : int
        Number of points along the crack front.

    Returns
    -------
    tuple
        (phi_deg, Y)
    """

    import numpy as np

    phi_deg = np.linspace(0.0, 90.0, points)

    Y = np.zeros(points)

    for i, angle in enumerate(phi_deg):

        phi = np.radians(angle)

        Yt, _ = corner_surface_crack(
            a,
            c,
            b,
            t,
            phi,
        )

        Y[i] = Yt

    return phi_deg, Y