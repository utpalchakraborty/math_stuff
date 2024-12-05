import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
sns.set_style("whitegrid")
# Use a custom color palette - we'll use 'rocket' for a dramatic look
custom_palette = sns.color_palette("rocket")
sns.set_palette(custom_palette)

# Create the parameter space
# The Enneper surface is typically parameterized over a square domain
u = np.linspace(-2, 2, 200)
v = np.linspace(-2, 2, 200)
U, V = np.meshgrid(u, v)

# Calculate the surface coordinates using the Enneper surface parameterization
# These are derived from the Weierstrass-Enneper representation
X = U - (U**3) / 3 + U * V**2
Y = V - (V**3) / 3 + V * U**2
Z = U**2 - V**2

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(
    elev=35, azim=45
)  # Adjusted viewing angle to showcase the self-intersections

# Create the surface plot
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="rocket",  # Using rocket colormap for dramatic effect
    alpha=0.8,
    linewidth=0,
    antialiased=True,
)

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Enneper Surface (Minimal Surface)", pad=20, fontsize=14)

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
