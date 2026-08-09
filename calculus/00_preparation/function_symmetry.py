"""Plot an even function, an odd function, and a function with neither symmetry."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 400)

y_even = x**2
y_odd = x**3
y_neither = x**2 + x

plt.plot(x, y_even, label="even: x^2")
plt.plot(x, y_odd, label="odd: x^3")
plt.plot(x, y_neither, label="neither: x^2 + x")

plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.xlim(-3, 3)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Symmetry")
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()

output_path = Path("function_symmetry.png")
plt.savefig(output_path, dpi=160)
print(f"saved: {output_path.resolve()}")
