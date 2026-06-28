"""
plot_geometry.py

High-level plotting interface for FractureTools.

These functions generate engineering plots for each crack geometry
using the geometry-specific curve generators.
"""

from math import radians

from .plotting import (
    plot_geometry_factor,
    plot_phi_curve,
)

from .geometries import (
    center_curve,
    center_through_crack,
    edge_curve,
    single_edge_through_crack,
    elliptical_curve,
    elliptical_surface_crack,
    corner_curve,
    corner_surface_crack,
    thumbnail_curve,
    thumbnail_crack,
)


def plot_center(a, b):
    """
    Plot center through crack geometry factor.
    """

    x, y = center_curve()

    ratio = a / b

    Yt, _ = center_through_crack(a, b)

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=ratio,
        y_point=Yt,
        title="Center Through Crack",
        xlabel="a / b",
    )


def plot_edge(a, b):
    """
    Plot single edge crack geometry factor.
    """

    x, y = edge_curve()

    ratio = a / b

    Yt, _ = single_edge_through_crack(a, b)

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=ratio,
        y_point=Yt,
        title="Single Edge Through Crack",
        xlabel="a / b",
    )


def plot_elliptical(
    a,
    c,
    b,
    t,
    phi,
):
    """
    Plot elliptical surface crack geometry factor.
    """

    phi_curve, y = elliptical_curve(
        a,
        c,
        b,
        t,
    )

    Yt, _ = elliptical_surface_crack(
        a,
        c,
        b,
        t,
        radians(phi),
    )

    plot_phi_curve(
        phi=phi_curve,
        Y=y,
        phi_point=phi,
        Y_point=Yt,
        title="Elliptical Surface Crack",
    )


def plot_corner(
    a,
    c,
    b,
    t,
    phi,
):
    """
    Plot corner surface crack geometry factor.
    """

    phi_curve, y = corner_curve(
        a,
        c,
        b,
        t,
    )

    Yt, _ = corner_surface_crack(
        a,
        c,
        b,
        t,
        radians(phi),
    )

    plot_phi_curve(
        phi=phi_curve,
        Y=y,
        phi_point=phi,
        Y_point=Yt,
        title="Corner Surface Crack",
    )


def plot_thumbnail(
    a,
    diameter,
):
    """
    Plot thumbnail crack geometry factor.
    """

    x, y = thumbnail_curve(
        diameter,
    )

    ratio = a / diameter

    Yt, _ = thumbnail_crack(
        a,
        diameter,
    )

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=ratio,
        y_point=Yt,
        title="Thumbnail Crack in Solid Cylinder",
        xlabel="a / D",
    )

    