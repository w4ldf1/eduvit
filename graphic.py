import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="green", linewidth=2, label="sin(x)")
plt.title("График функции y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
