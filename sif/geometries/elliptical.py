"""
Elliptical Surface Crack Geometry

Reference
---------
MechaniCalc Stress Intensity Factor Solutions

Returns geometry correction factors only.
"""

from math import cos, pi, sin, sqrt


def sec(x: float) -> float:
    """Return sec(x) where x is in radians."""
    return 1.0 / cos(x)


def elliptical_surface_crack(
    a: float,
    c: float,
    b: float,
    t: float,
    phi: float,
) -> tuple[float, float]:
    """
    Calculate geometry correction factors for an elliptical
    surface crack in a finite-width plate.

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

    # Shape factor
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

        M1 = 1.13 - 0.09 * (a / c)

        M2 = -0.54 + 0.89 / (0.20 + a / c)

        M3 = (
            0.50
            - 1.0 / (0.65 + a / c)
            + 14.0 * (1.0 - a / c) ** 24
        )

        g = (
            1.0
            + (
                0.10
                + 0.35 * (a / t) ** 2
            )
            * (1.0 - sin(phi)) ** 2
        )

        F = (
            (
                M1
                + M2 * (a / t) ** 2
                + M3 * (a / t) ** 4
            )
            * f_phi
            * f_w
            * g
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
        # This follows your MATLAB implementation.
        # We'll replace this branch with the complete
        # Newman-Raju equations later.
        #
        F = f_phi * f_w

    Y = F / sqrt(Q)

    return Y, Y


def elliptical_curve(
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

        Yt, _ = elliptical_surface_crack(
            a,
            c,
            b,
            t,
            phi,
        )

        Y[i] = Yt

    return phi_deg, Y