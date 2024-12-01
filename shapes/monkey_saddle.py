import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set the style using seaborn
sns.set_style("whitegrid")
# Use a custom color palette - we'll use 'plasma' for yet another distinct look
custom_palette = sns.color_palette("plasma")
sns.set_palette(custom_palette)

# Create the coordinate grid
# Using linspace with a wider range to show the interesting features
# We need more points for smoother curves due to the cubic function
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# Calculate Z values for our monkey saddle
# The equation z = x³ - 3xy² creates the monkey saddle shape
Z = X**3 - 3 * X * Y**2

# Create the figure with a specific size for better visibility
plt.figure(figsize=(12, 8))
# Add a 3D subplot with a specific viewing angle
ax = plt.axes(projection="3d")
ax.view_init(
    elev=30, azim=60
)  # Adjusted viewing angle to showcase the three depressions

# Create the surface plot
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="plasma",  # Using plasma colormap for a distinctive look
    alpha=0.8,
    linewidth=0,
    antialiased=True,
)

# Customize the appearance
ax.set_xlabel("X axis", labelpad=10, fontsize=12)
ax.set_ylabel("Y axis", labelpad=10, fontsize=12)
ax.set_zlabel("Z axis", labelpad=10, fontsize=12)
ax.set_title("Monkey Saddle Surface (z = x³ - 3xy²)", pad=20, fontsize=14)

# Add a color bar to show the height mapping
plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Height (z value)")

# Add some additional grid lines for better depth perception
ax.grid(True, linestyle="--", alpha=0.3)

# Adjust the layout to prevent cutting off any elements
plt.tight_layout()

# Display the plot
plt.show()
