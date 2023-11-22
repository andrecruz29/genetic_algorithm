import numpy as np
import matplotlib.pyplot as plt
from modules import AG
from matplotlib import cm
from matplotlib.ticker import LinearLocator

part = 40
x, y = np.arange(-3,13,(16/part)), np.arange(4.1,5.9,(1.8/part))
x, y = np.meshgrid(x,y)
z = AG.fitness(x,y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 40)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()