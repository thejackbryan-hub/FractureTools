"""
plotting.py

Plotting utilities for Stress Intensity Factor (SIF) calculations.

These functions generate geometry factor curves and highlight
the user's selected operating point.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_geometry_factor(
    x,
    y,
    x_point,
    y_point,
    title,
    xlabel,
    ylabel="Geometry Factor",
):
    """
    Plot a geometry factor curve.

    Parameters
    ----------
    x : array-like
        X-axis data.

    y : array-like
        Y-axis data.

    x_point : float
        User x-coordinate.

    y_point : float
        User y-coordinate.

    title : str
        Plot title.

    xlabel : str
        X-axis label.

    ylabel : str
        Y-axis label.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        x,
        y,
        linewidth=2,
        label="Geometry Factor",
    )

    plt.scatter(
        x_point,
        y_point,
        color="red",
        s=60,
        zorder=3,
        label="Current Value",
    )

    plt.grid(True)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.title(title)

    plt.legend()

    plt.tight_layout()

    plt.show()


def plot_phi_curve(
    phi,
    Y,
    phi_point,
    Y_point,
    title,
):
    """
    Plot geometry factor versus crack-front angle.

    Parameters
    ----------
    phi : array-like
        Angle values (degrees).

    Y : array-like
        Geometry factors.

    phi_point : float
        Selected angle.

    Y_point : float
        Selected geometry factor.

    title : str
        Plot title.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        phi,
        Y,
        linewidth=2,
        label="Geometry Factor",
    )

    plt.scatter(
        phi_point,
        Y_point,
        color="red",
        s=60,
        zorder=3,
        label="Current Value",
    )

    plt.grid(True)

    plt.xlabel("Crack Front Angle (degrees)")

    plt.ylabel("Geometry Factor")

    plt.title(title)

    plt.legend()

    plt.tight_layout()

    plt.show()


def create_ratio_array(
    minimum=0.001,
    maximum=0.95,
    points=500,
):
    """
    Generate a ratio array for plotting.

    Returns
    -------
    numpy.ndarray
    """

    return np.linspace(
        minimum,
        maximum,
        points,
    )


def create_phi_array():
    """
    Generate crack-front angle array.

    Returns
    -------
    numpy.ndarray
        0 to 90 degrees.
    """

    return np.linspace(
        0.0,
        90.0,
        181,
    )
