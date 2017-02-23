import numpy as np
from numpy.linalg import norm
from scipy.constants import g

unit_i = np.array([1.0, 0.0])
unit_j = np.array([0.0, 1.0])


def angle_between(v1, v2):
    costheta = np.dot(v1, v2)/norm(v1)/norm(v2)
    return np.arccos(costheta)


class Pendulum:

    def __init__(self, length, theta, mass):
        self.mass = mass
        self.theta = theta
        self.length = length
        self.acceleration = np.array([0.0, 0.0])  # Z component
        self.velocity = np.array([0.0, 0.0])      # Z component
        self.I = self.mass * length ** 2
        self.prev = None
        self.next = None

        self.moment =\
            self.length * np.array([np.sin(self.theta), np.cos(self.theta)])

    def attach_to(self, pendulum):
        self.prev = pendulum
        pendulum.next = self

    def gravity(self):
        return unit_j * self.mass * g

    def update_moment(self):
        self.moment =\
            self.length * np.array([np.sin(self.theta), np.cos(self.theta)])

    def tension(self):
        tension_mag = self.mass * g * np.cos(self.theta)\
                      + self.mass *\
                      norm(self.velocity) ** 2/self.length

        if self.next:
            tension_mag -= norm(self.next.tension()) *\
                    np.cos(-self.theta + self.next.theta)

        # print("Grav", self.mass * g * np.cos(self.theta))
        # print("Tension", tension_mag)
        # print("Cent", self.mass * norm(self.velocity)**2 / self.length)
        return np.abs(tension_mag) * -self.moment/norm(self.moment)

    def update_acceleration(self, dt):
        gravity = self.gravity()
        tension = self.tension()
        net_force = gravity + tension
        if self.next is not None:
            tension += -self.next.tension()

        self.acceleration = net_force/self.mass

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt
        # if self.prev:
        #     self.velocity += self.prev.velocity

    def update_position(self, dt):
        print("Old theta", self.theta)

        self.moment += self.velocity * dt
        self.moment *= self.length/norm(self.moment)
        self.theta = angle_between(self.moment, unit_j)
        if self.moment[0] < 0 and not self.theta < 0:
            self.theta *= -1
        elif self.moment[0] > 0 and not self.theta > 0:
            self.theta *= -1

        print("New theta", self.theta)

    def update_velocity_and_position(self, dt):
        # print("Old Moment", self.moment)
        # print("Old Theta", np.rad2deg(self.theta))
        # print("length/moment", self.length/norm(self.moment))

        self.update_moment()
        self.update_acceleration(dt)
        self.update_velocity(dt)
        self.update_position(dt)

        # print("New Moment", self.moment)
        # print("Moment X", self.moment[0])
        # print("Moment y", self.moment[1])
