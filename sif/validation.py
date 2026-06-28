"""
validation.py

Input validation functions for Stress Intensity Factor (SIF)
calculations.

These functions verify that user inputs are physically meaningful
before calculations are performed.
"""

from math import pi


def positive(value: float, name: str) -> None:
    """
    Ensure a value is positive.

    Parameters
    ----------
    value : float
        Value to validate.

    name : str
        Variable name used in error messages.
    """

    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")


def non_negative(value: float, name: str) -> None:
    """
    Ensure a value is non-negative.
    """

    if value < 0:
        raise ValueError(f"{name} cannot be negative.")


def angle(phi: float) -> None:
    """
    Validate crack-front angle.

    Parameters
    ----------
    phi : float
        Crack-front angle in radians.

    Notes
    -----
    Valid range:

        0 <= phi <= pi/2
    """

    if phi < 0 or phi > pi / 2:
        raise ValueError(
            "phi must be between 0 and pi/2 radians."
        )


def stress(value: float, name: str) -> None:
    """
    Validate applied stress.

    Compression is allowed.

    Parameters
    ----------
    value : float

    name : str
    """

    if abs(value) > 1.0e9:
        raise ValueError(
            f"{name} appears unrealistically large."
        )


def ratio_less_than_one(
    numerator: float,
    denominator: float,
    numerator_name: str,
    denominator_name: str,
) -> None:
    """
    Ensure a geometric ratio is less than one.

    Example
    -------
        a/b < 1
    """

    if numerator >= denominator:
        raise ValueError(
            f"{numerator_name} must be smaller than {denominator_name}."
        )


def crack_geometry(
    a: float,
    b: float,
    thickness: float | None = None,
    c: float | None = None,
) -> None:
    """
    Validate common crack geometry inputs.

    Parameters
    ----------
    a : float
        Crack depth or half-length.

    b : float
        Plate width or cylinder diameter.

    thickness : float, optional
        Plate thickness.

    c : float, optional
        Crack half-length.
    """

    positive(a, "Crack size (a)")
    positive(b, "Width (b)")

    ratio_less_than_one(
        a,
        b,
        "a",
        "b",
    )

    if thickness is not None:
        positive(
            thickness,
            "Thickness",
        )

    if c is not None:
        positive(
            c,
            "Half crack length (c)",
        )
