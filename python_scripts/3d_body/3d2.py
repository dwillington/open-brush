import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define masses and initial positions
m1, m2 = 1, 2  # Masses of the bodies
x1, y1, z1 = 0, 0, 1  # Initial position of body 1
x2, y2, z2 = 2, 0, 0  # Initial position of body 2

# Simulation parameters (adjust for desired animation)
dt = 0.01  # Time step
total_time = 10  # Total simulation time

# Initialize positions and velocities
positions = np.array([[x1, y1, z1], [x2, y2, z2]])  # Initial positions
positions = positions.astype(float)  # Convert to floating-point type
velocities = np.zeros((2, 3))  # Initial velocities are zero

# Function to calculate gravitational force
def gravity_force(m1, m2, r1, r2):
  G = 6.6743e-11  # Gravitational constant
  r = r2 - r1
  distance = np.linalg.norm(r)
  return G * m1 * m2 * r / (distance**3)

# Main animation loop
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-3, 3)
ax.set_ylim3d(-3, 3)
ax.set_zlim3d(-3, 3)

# Plot initial positions
body1, = ax.plot([x1], [y1], [z1], 'o', markersize=10, markerfacecolor='red', markeredgewidth=2)
body2, = ax.plot([x2], [y2], [z2], 'o', markersize=10, markerfacecolor='blue', markeredgewidth=2)

# Animation loop
for t in np.arange(0, total_time, dt):
  # Update forces and velocities
  force1 = gravity_force(m1, m2, positions[0], positions[1])
  force2 = -force1  # Gravitational force is mutual
  velocities += dt * np.array([force1 / m1, force2 / m2])

  # Update positions
  positions += dt * velocities

  # Update plot data

  # Check your Matplotlib version for the appropriate method:
  # Newer Matplotlib versions (use set_data)
  # body1.set_data(positions[0, :2], positions[0, 2])
  # body2.set_data(positions[1, :2], positions[1, 2])

  body1.set_data(positions[0, :2], positions[0, 2])  # Pass x and y as tuple, z separately
  body2.set_data(positions[1, :2], positions[1, 2])

  # Draw vectors (adjust scaling and style as needed)
  arrow1 = ax.arrow(positions[0, 0], positions[0, 1], positions[0, 2], 
                    velocities[0, 0], velocities[0, 1], velocities[0, 2],
                    color='red', linewidth=2)
  arrow2 = ax.arrow(positions[1, 0], positions[1, 1], positions[1, 2], 
                    velocities[1, 0], velocities[1, 1], velocities[1, 2],
                    color='blue', linewidth=2)

  # Clear previous arrows for smoother animation
  ax.clear_arrow3d(arrow1)
  ax.clear_arrow3d(arrow2)

  plt.pause(0.001)  # Adjust pause time for desired animation speed

plt.show()
