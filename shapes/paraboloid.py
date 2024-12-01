import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
# The 'whitegrid' style gives us a clean, modern look that's easy to read
sns.set_style("whitegrid")
# Use a custom color palette - we'll choose a sequential palette that works well for 3D
custom_palette = sns.color_palette("viridis")
sns.set_palette(custom_palette)

# Create the coordinate grid
# We use linspace to create evenly spaced points from -2 to 2
# 100 points gives us smooth curves while still being computationally efficient
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
# meshgrid creates a 2D grid from our 1D coordinate arrays
X, Y = np.meshgrid(x, y)

# Calculate Z values for our paraboloid
# The equation z = x² + y² creates the classic paraboloid shape
Z = X**2 + Y**2

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(elev=30, azim=45)  # 30 degree elevation, 45 degree azimuth

# Create the surface plot
# alpha controls transparency - 0.8 lets us see the surface structure clearly
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="viridis",  # This colormap transitions smoothly from dark to light
    alpha=0.8,
    linewidth=0,  # Remove grid lines for a smoother look
    antialiased=True,
)  # Smooth out the rendering

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Paraboloid Surface (z = x² + y²)", pad=20, fontsize=14)

# Add a color bar to show the height mapping
plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Height (z value)")

# Adjust the layout to prevent cutting off any elements
plt.tight_layout()

# Display the plot
plt.show()
