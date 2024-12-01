import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
sns.set_style("whitegrid")
# Use a custom color palette - we'll use 'magma' for a different look than yesterday
custom_palette = sns.color_palette("magma")
sns.set_palette(custom_palette)

# Create the coordinate grid
# Using linspace to create evenly spaced points from -2 to 2
# 100 points gives us smooth curves while still being computationally efficient
x = np.linspace(-3, 3, 150)
y = np.linspace(-3, 3, 150)
X, Y = np.meshgrid(x, y)

# Calculate Z values for our hyperbolic paraboloid
# The equation z = y² - x² creates the saddle shape
Z = Y**2 - X**2

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(elev=25, azim=45)  # Adjusted viewing angle to better show the saddle shape

# Create the surface plot
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="magma",  # Using magma colormap for a different aesthetic
    alpha=0.8,
    linewidth=0,
    antialiased=True,
)

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Hyperbolic Paraboloid (z = y² - x²)", pad=20, fontsize=14)

# Add a color bar to show the height mapping
plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Height (z value)")

# Add some additional grid lines for better depth perception
ax.grid(True, linestyle="--", alpha=0.3)

# Adjust the layout to prevent cutting off any elements
plt.tight_layout()

# Display the plot
plt.show()
