"""
ENGPHYS213 Final Project
Author: Viraj Bangari
"""


if __name__ == "__main__":
    import pendulum
    import matplotlib.pyplot as plt
    import numpy as np

    number_of_points = 10000
    time_start = 0
    time_end = 10
    initial_angles = np.array([180, 175])
    initial_omegas = np.array([0, 0])
    mass = np.array([10, 10])
    length = np.array([1, 1])

    times, theta = pendulum.simulate(time_start, time_end, initial_angles,
                                     initial_omegas, mass, length,
                                     number_of_points)
    plt.plot(times, theta[0],
             label="m = {} kg, θi = {}, ⍵i = {}".format(
                 mass[0], initial_angles[0], initial_omegas[0]))
    plt.plot(times, theta[1],
             label="m = {} kg, θi = {}, ⍵i = {}".format(
                 mass[1], initial_angles[1], initial_omegas[1]))

    plt.title("Simulation of Double Pendulum with {} points".format(
        number_of_points))
    plt.xlabel("Time [s]")
    plt.ylabel("Angle [rad]")

    plt.legend()
    plt.show()
