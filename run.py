"""
ENGPHYS213 Final Project
Author: Viraj Bangari

The coupled equations for the ODE are:
a0 * theta1_tt + a1 * theta0_tt + a2 * theta0_t**2 + a3 = 0
b0 * theta0_tt + b1 * theta1_tt + b2 * theta1_t**2 + b3

where:
a[0] = mass[1]*length[1]**2
a[1] = mass[1]*length[0] * cos(theta[0][i] - theta[1][i])
a[2] = -mass[1]*length[0] * sin(theta[0][i] - theta[1][i])
a[3] = mass[1]*g * sin(theta[1][i])

b[0] = (mass[0] + mass[1])*length[0]
b[1] = mass[1]*length[1]*cos(theta[0][i] - theta[1][i])
b[2] = mass[1]*length[1]*sin(theta[0][i] - theta[1][i])
b[3] = g * (mass[0] + mass[1])*sin(theta[0][i])
(source: http://scienceworld.wolfram.com/physics/DoublePendulum.html)


The differential terms can be calculated by:
theta_tt = (theta[i+1] - 2*theta[i] + theta[i-1])/time_step**2
theta_t = (theta[i] - theta[i-1])/time_step
(Note, the reason I do this for theta_t is to simplify the math)

If you multiply each side by time_step**2, and taylor approximate
theta_t

theta_tt = theta[n][i+1] - 2*theta[n][i] + theta[n][i-1]

a0 * theta[1][i+1] + a1*theta[0][i] + d0 = 0
b0 * theta[0][i+1] + b1*theta[1][i] + d1 = 0

Then, the d term can be subtracted. The two theta terms can be
eliminated using a matrix.

"""


import numpy as np
from numpy import sin, cos
from constants import g
import matplotlib.pyplot as plt


def set_initial_conditions(theta, initial_angle, initial_omega, time_step):
    theta[:, 1] = np.deg2rad(initial_angle[:])
    theta[:, 0] = theta[:, 1] - initial_omega[:] * time_step


def dterm_2nddiff(theta, i):
    return -2*theta[i] + theta[i-1]


def dterm_1stdiff(theta, i):
    return (theta[i] - theta[i-1])**2


def _d_term(theta1, theta2, a, i):
    return a[0] * dterm_2nddiff(theta1, i)\
            + a[1] * dterm_2nddiff(theta2, i)\
            + a[2] * dterm_1stdiff(theta2, i)\
            + a[3]


def get_results(time_start, time_end, initial_angles,
                initial_omegas, mass, length):

    theta = np.zeros((2, number_of_points))
    times = np.linspace(time_start, time_end, number_of_points)
    time_step = (time_start + time_end)/number_of_points
    set_initial_conditions(theta, initial_angles, initial_omegas, time_step)

    a = np.zeros(4)
    b = np.zeros(4)
    d = np.zeros(2)
    for i in range(1, number_of_points - 1):
        a[0] = (mass[0] + mass[1])*length[0]
        a[1] = mass[1]*length[1] * cos(theta[0][i] - theta[1][i])
        a[2] = mass[1]*length[1] * sin(theta[0][i] - theta[1][i])
        a[3] = g*(mass[0] + mass[1])*sin(theta[0][i]) * time_step**2

        b[0] = mass[1]*length[1]**2
        b[1] = mass[1]*length[0] * cos(theta[0][i] - theta[1][i])
        b[2] = -mass[1]*length[0] * sin(theta[0][i] - theta[1][i])
        b[3] = mass[1]*g * sin(theta[1][i]) * time_step**2

        d[0] = _d_term(theta[0], theta[1], a, i)
        d[1] = _d_term(theta[1], theta[0], b, i)

        # Matrix returns theta 0, then theta1
        ab_matrix = np.array([[a[0], a[1]],
                              [b[1], b[0]]])

        theta[0][i+1], theta[1][i+1] = np.linalg.solve(ab_matrix, -d)

    return times, theta


if __name__ == "__main__":
    number_of_points = 10000
    time_start = 0
    time_end = 10
    initial_angles = np.array([90, 90])
    initial_omegas = np.array([0, 0])
    mass = np.array([0.1, 100])
    length = np.array([1, 1])

    times, theta = get_results(time_start, time_end, initial_angles,
                               initial_omegas, mass, length)

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
