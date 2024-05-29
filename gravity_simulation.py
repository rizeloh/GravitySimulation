import matplotlib.pyplot as plt

def simulate_gravity(initial_height, time_step=0.1, total_time=10):
    """
    Simulate the motion of an object under the influence of gravity.

    Parameters:
    initial_height (float): The initial height of the object in meters.
    time_step (float): The time step for the simulation in seconds. Default is 0.1 seconds.
    total_time (float): The total time for the simulation in seconds. Default is 10 seconds.

    Returns:
    list: A list of (time, height) tuples representing the motion of the object.
    """
    g = 9.81  # Acceleration due to gravity in m/s^2
    t = 0  # Initial time
    h = initial_height  # Initial height

    motion_data = []

    while t <= total_time and h >= 0:
        motion_data.append((t, h))
        t += time_step
        h -= 0.5 * g * t**2

    return motion_data

def plot_motion(motion_data):
    """
    Plot the motion of the object.

    Parameters:
    motion_data (list): A list of (time, height) tuples representing the motion of the object.

    Returns:
    None
    """
    times, heights = zip(*motion_data)

    plt.figure(figsize=(10, 5))
    plt.plot(times, heights, label="Height over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Motion of an Object under Gravity")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage
    initial_height = 100  # Initial height in meters
    motion_data = simulate_gravity(initial_height)

    plot_motion(motion_data)
