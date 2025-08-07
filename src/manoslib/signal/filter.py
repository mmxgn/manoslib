import numpy as np
import scipy.signal


def calculate_order(att: float, wb: float) -> float:
    """
    Calculates the order of a FIR lowpass filter using the kaiser window approach

    Arguments:
     - att: The attenuation in dB. Positive float.
     - wb:  The transition period in normalized w frequency.
    """
    return int((att - 7.95) / (14.36 * wb))


def get_taps(wc: float, wb: float, att: float) -> np.ndarray:
    """
    Gets the impulse response of a FIR filter with a cutoff frequency wc and a transition bandwidth wb
    where both wc and wb are in normalized frequency units (a value of 1 is the Nyquist frequency). `att`
    is the stopband attenuation.
    """
    ord, beta = scipy.signal.kaiserord(att, wb)
    ord = calculate_order(att, wb)
    taps = scipy.signal.firwin(ord, wc, window=("kaiser", beta), fs=2)
    return taps
