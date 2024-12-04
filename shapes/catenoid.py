import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
sns.set_style("whitegrid")
# Use a custom color palette - we'll use 'coolwarm' for a nice symmetric look
custom_palette = sns.color_palette("coolwarm")
sns.set_palette(custom_palette)

# Create the parameter space
# u is the rotation parameter (0 to 2π)
# v controls the height and curvature
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-2, 2, 100)
U, V = np.meshgrid(u, v)

# Scaling factor for the catenoid
a = 1.0

# Calculate the surface coordinates
# x = a*cosh(v)*cos(u)
# y = a*cosh(v)*sin(u)
# z = a*v
X = a * np.cosh(V) * np.cos(U)
Y = a * np.cosh(V) * np.sin(U)
Z = a * V

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(elev=20, azim=45)  # Adjusted viewing angle to showcase the catenoid shape

# Create the surface plot
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="coolwarm",  # Using coolwarm colormap for a symmetric look
    alpha=0.8,
    linewidth=0,
    antialiased=True,
)

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Catenoid Surface (Minimal Surface of Revolution)", pad=20, fontsize=14)

# Add a color bar to show the height mapping
plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Height (z value)")

# Make the plot more symmetric by setting equal aspect ratio
ax.set_box_aspect([1, 1, 1])

# Add some additional grid lines for better depth perception
ax.grid(True, linestyle="--", alpha=0.3)

# Adjust the layout to prevent cutting off any elements
plt.tight_layout()

# Display the plot
plt.show()
