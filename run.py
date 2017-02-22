from pendulum import Pendulum
import numpy as np
import matplotlib.pyplot as plt

simple = Pendulum(1, np.pi/2, 10)
simple2 = Pendulum(1, np.pi/2, 10)


t = 0
dt = 0.01
ts = []
thetas = []
while t < 3:
    simple.add_forces(simple.gravity(), simple.tension())
    simple2.add_forces(simple2.gravity(), simple2.tension(), -simple.tension())

    simple.update_velocity_and_position(dt)
    simple2.update_velocity_and_position(dt)

    ts.append(t)
    thetas.append(np.rad2deg(simple.theta))
    t += dt

plt.plot(ts, thetas)
plt.show()
