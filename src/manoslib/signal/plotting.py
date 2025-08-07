import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


def plot_responses(
    h_i: np.ndarray,
    log_db: bool = True,
    fig=None,
    ax: np.ndarray = None,
    x_lim: float | None = None,
    y_lim: float | None = None,
) -> tuple:
    """
    Plots the impulse, frequency, and phase responses of the FIR `h_i`
    """
    w, h = scipy.signal.freqz(h_i)

    if not (fig or ax):
        fig, ax = plt.subplots(2)
    ax[0].plot(h_i, label="ir")
    if log_db:
        ax[1].plot(w / np.pi, 20 * np.log10(np.abs(h) + 10e-20), label="magnitude")
    else:
        ax[1].plot(w / np.pi, np.abs(h), label="magnitude")

    ax[1].twinx().plot(
        w / np.pi, np.unwrap(np.angle(h)), color="red", alpha=0.4, label="phase"
    )

    if y_lim:
        ax[1].set_ylim(y_lim)

    return fig, ax
