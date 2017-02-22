from pendulum import Pendulum
import matplotlib.pyplot as plt
import numpy as np
from math import pi

p1 = Pendulum(1, np.deg2rad(10), 10)
# p2 = Pendulum(1, 0, 10)
# p1.attach_to(p2)


t = 0
dt = 0.1
ts = []
p1theta = []
p1v = []
p2theta = []
while t < 1.2:
    print("_____")
    print("t = ", t)
    ts.append(t)
    p1.update_velocity_and_position(dt)
    p1theta.append(np.rad2deg(p1.theta))
    p1v.append(np.linalg.norm(p1.velocity))

    # p2.update_velocity_and_position(dt)
    # p2theta.append(p2.theta)
    t += dt

# plt.plot(ts, p1theta, label="p1")
plt.plot(ts, p1v, label="p1")
# plt.plot(ts, p2theta, label="p2")
plt.legend()
plt.show()
