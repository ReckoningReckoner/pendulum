from pendulum import Pendulum
import matplotlib.pyplot as plt
import numpy as np
from math import pi

p1 = Pendulum(1, np.deg2rad(90), 10)
p2 = Pendulum(1, np.deg2rad(90), 1)

p2.attach_to(p1)

t = 0
dt = 0.01
ts = []
p1theta = []
p1v = []
p2theta = []
while t < 100:
    print("_____")
    print("t = ", t)
    ts.append(t)
    p1.update_velocity_and_position(dt)
    p2.update_velocity_and_position(dt)

    p1theta.append(np.rad2deg(p1.theta))
    p2theta.append(np.rad2deg(p2.theta))

    t += dt

plt.plot(ts, p1theta, "-", label="p1")
plt.plot(ts, p2theta, "-", label="p2")
plt.legend()
plt.show()
