import numpy as np
from scipy.constants import g


class Pendulum:

    def __init__(self, length, theta, mass):
        self.mass = mass
        self.theta = theta
        self.length = length
        self.acceleration = 0  # Z component
        self.velocity = 0      # Z component
        self.I = self.mass * length ** 2

    def moment(self):
        return np.array([self.length * np.sin(self.theta),
                         self.length * np.cos(self.theta)])

    def tension(self):
        moment = self.moment()
        linear_velocity = self.velocity * self.length
        tension =\
            self.mass * linear_velocity**2/self.length\
            - self.mass * g * np.cos(self.theta)

        return tension * -moment/np.linalg.norm(moment)

    def gravity(self):
        return np.array([0.0, self.mass * g])

    def add_forces(self, *forces):
        net_torque = 0  # in Z
        moment = self.moment()
        for force in forces:
            torque = np.cross(moment, force)
            net_torque += torque

        self.acceleration = net_torque/self.I

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt

    def update_position(self, dt):
        self.theta -= self.velocity * dt

    def update_velocity_and_position(self, dt):
        self.update_velocity(dt)
        self.update_position(dt)
