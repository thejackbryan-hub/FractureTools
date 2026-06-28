"""
examples.py

Example calculations for the Stress Intensity Factor (SIF) library.

Run:

    python3 -m sif.examples
"""

from math import radians

from .calculator import calculate_sif

from .plotting import (
    plot_geometry_factor,
    plot_phi_curve,
)

from .geometries.center import center_curve
from .geometries.edge import edge_curve
from .geometries.elliptical import elliptical_curve
from .geometries.corner import corner_curve
from .geometries.thumbnail import thumbnail_curve


def print_results(title: str, results: dict) -> None:
    """
    Print calculation results.
    """

    print("=" * 60)
    print(title)
    print("=" * 60)

    print(f"Geometry : {results['geometry']}")
    print(f"Yt       : {results['Yt']:.6f}")
    print(f"Yb       : {results['Yb']:.6f}")
    print(f"KI       : {results['KI']:.3f} psi√in")
    print(f"KI       : {results['KI_ksi']:.3f} ksi√in")
    print()


def main():

    # ==========================================================
    # Center Through Crack
    # ==========================================================

    center = calculate_sif(
        geometry="center",
        a=0.10,
        b=6.00,
        sigma_t=10000,
        sigma_b=5000,
    )

    print_results(
        "Center Through Crack",
        center,
    )

    x, y = center_curve()

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=0.10 / 6.00,
        y_point=center["Yt"],
        title="Center Through Crack",
        xlabel="a / b",
        ylabel="Yt",
    )

    # ==========================================================
    # Single Edge Through Crack
    # ==========================================================

    edge = calculate_sif(
        geometry="edge",
        a=0.50,
        b=6.00,
        sigma_t=12000,
        sigma_b=3000,
    )

    print_results(
        "Single Edge Through Crack",
        edge,
    )

    x, y = edge_curve()

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=0.50 / 6.00,
        y_point=edge["Yt"],
        title="Single Edge Through Crack",
        xlabel="a / b",
        ylabel="Yt",
    )

    # ==========================================================
    # Elliptical Surface Crack
    # ==========================================================

    elliptical = calculate_sif(
        geometry="elliptical",
        a=0.25,
        c=0.50,
        b=6.00,
        t=1.00,
        phi=radians(45),
        sigma_t=10000,
        sigma_b=5000,
    )

    print_results(
        "Elliptical Surface Crack",
        elliptical,
    )

    phi, Y = elliptical_curve(
        a=0.25,
        c=0.50,
        b=6.00,
        t=1.00,
    )

    plot_phi_curve(
        phi=phi,
        Y=Y,
        phi_point=45.0,
        Y_point=elliptical["Yt"],
        title="Elliptical Surface Crack",
    )

    # ==========================================================
    # Corner Surface Crack
    # ==========================================================

    corner = calculate_sif(
        geometry="corner",
        a=0.25,
        c=0.50,
        b=6.00,
        t=1.00,
        phi=radians(45),
        sigma_t=10000,
        sigma_b=5000,
    )

    print_results(
        "Corner Surface Crack",
        corner,
    )

    phi, Y = corner_curve(
        a=0.25,
        c=0.50,
        b=6.00,
        t=1.00,
    )

    plot_phi_curve(
        phi=phi,
        Y=Y,
        phi_point=45.0,
        Y_point=corner["Yt"],
        title="Corner Surface Crack",
    )

    # ==========================================================
    # Thumbnail Crack
    # ==========================================================

    thumbnail = calculate_sif(
        geometry="thumbnail",
        a=0.20,
        diameter=2.00,
        sigma_t=10000,
        sigma_b=5000,
    )

    print_results(
        "Thumbnail Crack",
        thumbnail,
    )

    x, y = thumbnail_curve(
        diameter=2.00,
    )

    plot_geometry_factor(
        x=x,
        y=y,
        x_point=0.20 / 2.00,
        y_point=thumbnail["Yt"],
        title="Thumbnail Crack in Solid Cylinder",
        xlabel="a / D",
        ylabel="Yt",
    )


if __name__ == "__main__":
    main()