"""
calculator.py

High-level interface for Stress Intensity Factor (SIF)
calculations.

Users should only need to call:

    calculate_sif(...)

This module handles:
    - input validation
    - geometry selection
    - geometry factor calculation
    - stress intensity calculation
"""

from .geometries import (
    center_through_crack,
    single_edge_through_crack,
    elliptical_surface_crack,
    corner_surface_crack,
    thumbnail_crack,
)

from .stress_intensity import (
    combined_mode_I,
    ksi_sqrt_in,
)

from .validation import (
    crack_geometry,
    stress,
    angle,
)


GEOMETRIES = {
    "center": center_through_crack,
    "edge": single_edge_through_crack,
    "elliptical": elliptical_surface_crack,
    "corner": corner_surface_crack,
    "thumbnail": thumbnail_crack,
}


def calculate_sif(geometry: str, **kwargs) -> dict:
    """
    Calculate the Mode I Stress Intensity Factor.

    Parameters
    ----------
    geometry : str

        Supported values

        center

        edge

        elliptical

        corner

        thumbnail

    Returns
    -------
    dict
    """

    geometry = geometry.lower()

    if geometry not in GEOMETRIES:
        raise ValueError(
            f"Unsupported geometry '{geometry}'."
        )

    # -------------------------------
    # Common inputs
    # -------------------------------

    sigma_t = kwargs["sigma_t"]
    sigma_b = kwargs["sigma_b"]

    stress(sigma_t, "sigma_t")
    stress(sigma_b, "sigma_b")

    # -------------------------------
    # Center Through Crack
    # -------------------------------

    if geometry == "center":

        a = kwargs["a"]
        b = kwargs["b"]

        crack_geometry(a, b)

        Yt, Yb = GEOMETRIES[geometry](a, b)

    # -------------------------------
    # Single Edge Crack
    # -------------------------------

    elif geometry == "edge":

        a = kwargs["a"]
        b = kwargs["b"]

        crack_geometry(a, b)

        Yt, Yb = GEOMETRIES[geometry](a, b)

    # -------------------------------
    # Elliptical Surface Crack
    # -------------------------------

    elif geometry == "elliptical":

        a = kwargs["a"]
        c = kwargs["c"]
        b = kwargs["b"]
        t = kwargs["t"]
        phi = kwargs["phi"]

        crack_geometry(a, b, t, c)
        angle(phi)

        Yt, Yb = GEOMETRIES[geometry](
            a,
            c,
            b,
            t,
            phi,
        )

    # -------------------------------
    # Corner Crack
    # -------------------------------

    elif geometry == "corner":

        a = kwargs["a"]
        c = kwargs["c"]
        b = kwargs["b"]
        t = kwargs["t"]
        phi = kwargs["phi"]

        crack_geometry(a, b, t, c)
        angle(phi)

        Yt, Yb = GEOMETRIES[geometry](
            a,
            c,
            b,
            t,
            phi,
        )

    # -------------------------------
    # Thumbnail Crack
    # -------------------------------

    elif geometry == "thumbnail":

        a = kwargs["a"]
        diameter = kwargs["diameter"]

        crack_geometry(a, diameter)

        Yt, Yb = GEOMETRIES[geometry](
            a,
            diameter,
        )

    # -------------------------------
    # Stress Intensity Factor
    # -------------------------------

    KI = combined_mode_I(
        Yt,
        Yb,
        sigma_t,
        sigma_b,
        a,
    )

    return {

        "geometry": geometry,

        "Yt": Yt,

        "Yb": Yb,

        "KI": KI,

        "KI_ksi": ksi_sqrt_in(KI),

    }
