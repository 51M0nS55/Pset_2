import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordinate conversion functions
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.array([x, y, z])

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return np.array([r, theta, phi])

def cylindrical_to_cartesian(rho, psi, z):
    x = rho * np.cos(psi)
    y = rho * np.sin(psi)
    return np.array([x, y, z])

def cartesian_to_cylindrical(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    psi = np.arctan2(y, x)
    return np.array([rho, psi, z])

# Visualization function
def plot_local_basis(theta, phi):
    # Unit sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.sin(v), np.cos(u))
    y = np.outer(np.sin(v), np.sin(u))
    z = np.outer(np.cos(v), np.ones_like(u))

    # Basis vectors at (theta, phi)
    e_r = np.array([np.sin(theta) * np.cos(phi),
                    np.sin(theta) * np.sin(phi),
                    np.cos(theta)])
    e_theta = np.array([np.cos(theta) * np.cos(phi),
                        np.cos(theta) * np.sin(phi),
                        -np.sin(theta)])
    e_phi = np.array([-np.sin(phi),
                      np.cos(phi),
                      0])
    origin = spherical_to_cartesian(1, theta, phi)

    # Plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='c', alpha=0.3)
    ax.quiver(*origin, *e_r, color='r', label=r"$\hat{e}_r$")
    ax.quiver(*origin, *e_theta, color='g', label=r"$\hat{e}_\theta$")
    ax.quiver(*origin, *e_phi, color='b', label=r"$\hat{e}_\phi$")
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Main function
if __name__ == "__main__":
    # Example conversion
    print("Cartesian to Spherical:", cartesian_to_spherical(1, 1, 1))
    print("Spherical to Cartesian:", spherical_to_cartesian(1, np.pi/4, np.pi/4))

    # Plot example
    theta = float(input("Enter theta (in radians): "))
    phi = float(input("Enter phi (in radians): "))
    plot_local_basis(theta, phi)
