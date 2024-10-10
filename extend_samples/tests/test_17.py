"""version 0.1.0"""
import random
import numpy as np
import pandas as pd
import matplotlib as plt
import mpl_toolkits
from extend_samples.src.get_plot_for_pdf import get_plot_for_pdf
from extend_samples.src.mosfet_function import mosfet_function


def create_coeffs() -> np.array:
    """
    Creates coeffs for test

    Returns
    -------
    np.array
    """
    array_shape = (9,)
    coeffs = np.zeros(array_shape)
    for i in range(array_shape[0]):
        coeffs[i] = random.uniform(0.0, 1.0)
    return coeffs


def generate_reference(
    device_number: int,
    channel_width: float,
    device_data_frame: pd.DataFrame,
    coeffs: np.array) -> (plt.figure.Figure, mpl_toolkits.mplot3d.axes3d.Axes3D):
    """
    Generate Reference plots

    Parameters
    ----------
    device_number: int
    channel_width: float
    device_data_frame: pd.DataFrame
    coeffs: np.array

    Returns
    -------
    tuple
    """
    fig = plt.pyplot.figure()

    ax = fig.add_subplot(111, projection='3d')

    x = np.array(device_data_frame.iloc[:, 1])
    y = np.array(device_data_frame.iloc[:, 2])
    z = np.array(device_data_frame.iloc[:, 3])

    ax.scatter(x, y, z, marker="o", label="orginal")

    z_reconstruction = np.zeros_like(z)
    for i in range(z_reconstruction.shape[0]):
        args = (x[i], y[i], channel_width)
        z_reconstruction[i] = mosfet_function(
            args,
            coeffs[0],
            coeffs[1],
            coeffs[2],
            coeffs[3],
            coeffs[4],
            coeffs[5],
            coeffs[6],
            coeffs[7],
            coeffs[8]
        )

    ax.scatter(x, y, z_reconstruction, label="reconstruction", marker="X")
    ax.legend()
    ax.set_title(f"Device {device_number}")
    ax.set_xlabel(r'$V_{ds}$')
    ax.set_ylabel(r'$V_{gs}$')
    ax.set_zlabel(r'$I_{ds}$')

    return fig, ax


def compare_titles(ax1: mpl_toolkits.mplot3d.axes3d.Axes3D, ax2: mpl_toolkits.mplot3d.axes3d.Axes3D) -> None:
    """
    Compare titles

    Parameters
    ----------
    ax1: mpl_toolkits.mplot3d.axes3d.Axes3D
    ax2: mpl_toolkits.mplot3d.axes3d.Axes3D
    """
    assert ax1.get_title() == ax2.get_title()


def compare_data(ax1: mpl_toolkits.mplot3d.axes3d.Axes3D, ax2: mpl_toolkits.mplot3d.axes3d.Axes3D) -> None:
    """
    Compare data series

    Parameters
    ----------
    ax1: mpl_toolkits.mplot3d.axes3d.Axes3D
    ax2: mpl_toolkits.mplot3d.axes3d.Axes3D
    """
    for line1, line2 in zip(ax1.get_lines(), ax2.get_lines()):
        np.testing.assert_array_equal(line1.get_xdata(), line2.get_xdata())
        np.testing.assert_array_equal(line1.get_ydata(), line2.get_ydata())
        np.testing.assert_array_equal(line1.get_zdata(), line2.get_zdata())


def compare_labels(ax1: mpl_toolkits.mplot3d.axes3d.Axes3D, ax2: mpl_toolkits.mplot3d.axes3d.Axes3D) -> None:
    """
    Compare labels

    Parameters
    ----------
    ax1: mpl_toolkits.mplot3d.axes3d.Axes3D
    ax2: mpl_toolkits.mplot3d.axes3d.Axes3D
    """
    assert ax1.get_xlabel() == ax2.get_xlabel()
    assert ax1.get_ylabel() == ax2.get_ylabel()
    assert ax1.get_zlabel() == ax2.get_zlabel()


def compare_legends(ax1: mpl_toolkits.mplot3d.axes3d.Axes3D, ax2: mpl_toolkits.mplot3d.axes3d.Axes3D) -> None:
    """
    Compare legends

    Parameters
    ----------
    ax1: mpl_toolkits.mplot3d.axes3d.Axes3D
    ax2: mpl_toolkits.mplot3d.axes3d.Axes3D
    """
    legend1 = [text.get_text() for text in ax1.get_legend().get_texts()]
    legend2 = [text.get_text() for text in ax2.get_legend().get_texts()]
    assert legend1 == legend2


def compare_linestyles(ax1: mpl_toolkits.mplot3d.axes3d.Axes3D, ax2: mpl_toolkits.mplot3d.axes3d.Axes3D) -> None:
    """
    Compare linestyles

    Parameters
    ----------
    ax1: mpl_toolkits.mplot3d.axes3d.Axes3D
    ax2: mpl_toolkits.mplot3d.axes3d.Axes3D
    """
    for line1, line2 in zip(ax1.get_lines(), ax2.get_lines()):
        assert line1.get_linestyle() == line2.get_linestyle()


def test_0():
    """
    Test 0

    Test plotting data
    """
    device_number = 1
    channel_width = 1e-6
    device_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 1.0, 6e-2, 4e-12]
    ]
    device_data_frame = pd.DataFrame(device_data)

    coeffs = create_coeffs()
    reference_fig, reference_ax = generate_reference(
        device_number,
        channel_width,
        device_data_frame,
        coeffs
    )

    fig, ax = get_plot_for_pdf(
        coeffs,
        device_number,
        device_data_frame,
        channel_width
    )

    compare_titles(reference_ax, ax)
    compare_data(reference_ax, ax)
    compare_labels(reference_ax, ax)
    compare_legends(reference_ax, ax)
    compare_linestyles(reference_ax, ax)
