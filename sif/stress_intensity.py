"""
stress_intensity.py

Mode I Stress Intensity Factor (SIF) calculations.

This module provides reusable functions for computing
Mode I stress intensity factors from geometry correction
factors.

Units
-----
If:
    Stress = psi
    Crack length = inches

Then:
    KI = psi * sqrt(in)

The helper function `ksi_sqrt_in()` converts the result
to ksi*sqrt(in).
"""

from math import pi, sqrt


def mode_I(
    Y: float,
    sigma: float,
    a: float,
) -> float:
    """
    Calculate the Mode I stress intensity factor.

    Parameters
    ----------
    Y : float
        Geometry correction factor.

    sigma : float
        Applied normal stress.

    a : float
        Crack length parameter.

    Returns
    -------
    float
        Stress intensity factor (psi*sqrt(in)).
    """

    return Y * sigma * sqrt(pi * a)


def combined_mode_I(
    Yt: float,
    Yb: float,
    sigma_t: float,
    sigma_b: float,
    a: float,
) -> float:
    """
    Calculate the Mode I stress intensity factor for
    combined tensile and bending loading.

    Parameters
    ----------
    Yt : float
        Tension geometry correction factor.

    Yb : float
        Bending geometry correction factor.

    sigma_t : float
        Tensile stress.

    sigma_b : float
        Bending stress.

    a : float
        Crack length parameter.

    Returns
    -------
    float
        Stress intensity factor (psi*sqrt(in)).
    """

    return (
        (Yt * sigma_t + Yb * sigma_b)
        * sqrt(pi * a)
    )


def tension_only(
    Yt: float,
    sigma_t: float,
    a: float,
) -> float:
    """
    Calculate Mode I SIF for tension only.

    Parameters
    ----------
    Yt : float
        Tension geometry correction factor.

    sigma_t : float
        Tensile stress.

    a : float
        Crack length parameter.

    Returns
    -------
    float
        Stress intensity factor.
    """

    return Yt * sigma_t * sqrt(pi * a)


def bending_only(
    Yb: float,
    sigma_b: float,
    a: float,
) -> float:
    """
    Calculate Mode I SIF for bending only.

    Parameters
    ----------
    Yb : float
        Bending geometry correction factor.

    sigma_b : float
        Bending stress.

    a : float
        Crack length parameter.

    Returns
    -------
    float
        Stress intensity factor.
    """

    return Yb * sigma_b * sqrt(pi * a)


def ksi_sqrt_in(
    KI: float,
) -> float:
    """
    Convert psi*sqrt(in) to ksi*sqrt(in).

    Parameters
    ----------
    KI : float
        Stress intensity factor in psi*sqrt(in).

    Returns
    -------
    float
        Stress intensity factor in ksi*sqrt(in).
    """

    return KI / 1000.0
