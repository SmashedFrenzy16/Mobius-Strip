import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
)

R = int(input("Enter in the R value of the Möbius strip: "))

t = np.linspace(0, (2 * np.pi), 100)
s = np.linspace(-1, 1, 100)
t, s = np.meshgrid(t, s)
x = (R + (s * np.cos(0.5 * t))) * np.cos(t)
y = (R + (s * np.cos(0.5 * 2))) * np.sin(t)
z = s * np.sin(0.5 * t)

figure = plt.figure()

ax = figure.add_subplot(111, projection="3d", facecolor="green")

ax.plot_surface(x, y, z, alpha=0.5)

ax.set_xlabel("𝑥")
ax.set_ylabel("𝑦")
ax.set_zlabel("𝑧")

ax.set_title("Möbius Strip Visualized")

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

plt.show()