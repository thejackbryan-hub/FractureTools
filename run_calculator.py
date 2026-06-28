"""
run_calculator.py

Interactive command-line interface for FractureTools.
"""

from sif.calculator import calculate_sif

from sif.plot_geometry import (
    plot_center,
    plot_edge,
    plot_elliptical,
    plot_corner,
    plot_thumbnail,
)


def main():

    print("=" * 60)
    print("FractureTools - Stress Intensity Factor Calculator")
    print("=" * 60)

    print("\nAvailable Geometries")
    print("--------------------")
    print("1 - Center Through Crack")
    print("2 - Single Edge Through Crack")
    print("3 - Elliptical Surface Crack")
    print("4 - Corner Surface Crack")
    print("5 - Thumbnail Crack")

    choice = input("\nSelect geometry (1-5): ")

    print()

    sigma_t = float(input("Tensile stress sigma_t (psi): "))
    sigma_b = float(input("Bending stress sigma_b (psi): "))

    # --------------------------------------------------
    # Center Crack
    # --------------------------------------------------

    if choice == "1":

        a = float(input("Crack half-length a (in): "))
        b = float(input("Plate half-width b (in): "))

        result = calculate_sif(
            geometry="center",
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            a=a,
            b=b,
        )

        plot_center(a, b)

    # --------------------------------------------------
    # Edge Crack
    # --------------------------------------------------

    elif choice == "2":

        a = float(input("Crack length a (in): "))
        b = float(input("Plate width b (in): "))

        result = calculate_sif(
            geometry="edge",
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            a=a,
            b=b,
        )

        plot_edge(a, b)

    # --------------------------------------------------
    # Elliptical Surface Crack
    # --------------------------------------------------

    elif choice == "3":

        a = float(input("Crack depth a (in): "))
        c = float(input("Half surface length c (in): "))
        b = float(input("Plate half-width b (in): "))
        t = float(input("Plate thickness t (in): "))
        phi = float(input("Crack-front angle φ (degrees): "))

        result = calculate_sif(
            geometry="elliptical",
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            a=a,
            c=c,
            b=b,
            t=t,
            phi=phi,
        )

        plot_elliptical(
            a,
            c,
            b,
            t,
            phi,
        )

    # --------------------------------------------------
    # Corner Crack
    # --------------------------------------------------

    elif choice == "4":

        a = float(input("Crack depth a (in): "))
        c = float(input("Half surface length c (in): "))
        b = float(input("Plate half-width b (in): "))
        t = float(input("Plate thickness t (in): "))
        phi = float(input("Crack-front angle φ (degrees): "))

        result = calculate_sif(
            geometry="corner",
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            a=a,
            c=c,
            b=b,
            t=t,
            phi=phi,
        )

        plot_corner(
            a,
            c,
            b,
            t,
            phi,
        )

    # --------------------------------------------------
    # Thumbnail Crack
    # --------------------------------------------------

    elif choice == "5":

        a = float(input("Crack depth a (in): "))
        diameter = float(input("Cylinder diameter (in): "))

        result = calculate_sif(
            geometry="thumbnail",
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            a=a,
            diameter=diameter,
        )

        plot_thumbnail(
            a,
            diameter,
        )

    else:

        raise ValueError("Invalid geometry selection.")

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    print("\n")
    print("=" * 60)
    print("Results")
    print("=" * 60)

    print(f"Geometry : {result['geometry']}")
    print(f"Yt       : {result['Yt']:.5f}")
    print(f"Yb       : {result['Yb']:.5f}")
    print(f"KI       : {result['KI']:.2f} psi√in")
    print(f"KI       : {result['KI_ksi']:.3f} ksi√in")


if __name__ == "__main__":
    main()
    