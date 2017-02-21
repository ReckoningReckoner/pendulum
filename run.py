from pendulum import Pendulum
import numpy as np
import matplotlib.pyplot as plt

simple = Pendulum(1, np.array([0, 0]), np.pi/3, 10)


t = 0
dt = 0.01
ts = []
thetas = []
while t < 10:
    simple.add_forces(simple.gravity(), simple.tension())
    simple.update_velocity_and_position(dt)
    ts.append(t)
    thetas.append(simple.theta)
    t += dt

plt.plot(ts, thetas)
plt.show()
