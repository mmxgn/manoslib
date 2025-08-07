# Design filter with specifications
# Sample rate: 20KHz
# Passband: 100Hz (wc = 0.03)
# Stopband: 300Hz (ws = 0.09)
# Transition: wb = 0.09 - 0.03 = 0.06
# Attenuation: 60dB

# 1. Compute order of filter
from manoslib.signal.filter import calculate_order


order = calculate_order(att=60, wb=0.06)
print(f"Filter order: {order}")

# 2. Design filter using the kaiser method
from manoslib.signal.filter import get_taps

h = get_taps(wc=0.03, wb=0.06, att=60)

# 3. Plot impulse and frequency responses
from manoslib.signal.plotting import plot_responses
import matplotlib.pyplot as plt
import matplotlib

fig, ax = plot_responses(h)
fig.suptitle("Responses of filter with $\\omega_c$=0.03, $\\omega_b$=0.09, A=60dB")
ax[0].set_title("Impulse response")
ax[1].set_title("Magnitude/Phase response")
ax[1].axhline(-60, color="red", linewidth=0.1, label="Attenuation line")
ax[1].axvline(
    0.03,
    color="red",
    linewidth=0.1,
)
ax[1].axvline(
    0.09,
    color="red",
    linewidth=0.1,
)
plt.savefig("responses.pdf")
