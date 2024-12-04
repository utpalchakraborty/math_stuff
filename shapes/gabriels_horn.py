import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
sns.set_style("whitegrid")
# Use a custom color palette - we'll use 'crest' for a beautiful blue gradient
custom_palette = sns.color_palette("crest")
sns.set_palette(custom_palette)

# Create the parameter space
# theta is the rotation parameter (0 to 2π)
# t controls the distance along the curve (1 to some finite value)
theta = np.linspace(0, 2 * np.pi, 100)
t = np.linspace(1, 10, 500)  # We'll cut off at x=5 for visualization
T, Theta = np.meshgrid(t, theta)

# Calculate the surface coordinates
# x = t
# y = (1/t)cos(θ)
# z = (1/t)sin(θ)
X = T
Y = (1 / T) * np.cos(Theta)
Z = (1 / T) * np.sin(Theta)

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(elev=20, azim=45)  # Adjusted viewing angle to showcase the horn shape

# Create the surface plot
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="crest",  # Using crest colormap for a nice blue gradient
    alpha=0.8,
    linewidth=0,
    antialiased=True,
)

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Gabriel's Horn (y = 1/x rotated around x-axis)", pad=20, fontsize=14)

# Add a color bar to show the height mapping
plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Distance from axis")

# Make the plot more symmetric by setting equal aspect ratio
ax.set_box_aspect([2, 1, 1])  # Adjusted to account for the horn's elongated shape

# Add some additional grid lines for better depth perception
ax.grid(True, linestyle="--", alpha=0.3)

# Adjust the layout to prevent cutting off any elements
plt.tight_layout()

# Display the plot
plt.show()
