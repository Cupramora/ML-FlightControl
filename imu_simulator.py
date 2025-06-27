# imu_simulator.py
# placeholder module for simulating IMU readings (accelerometer and gyroscope)

import math
import time

class IMUSimulator:
    """
    Provides mock accelerometer and gyroscope data for testing orientation fusion and PID loops.
    """

    def __init__(self):
        self.angle = 0.0
        self.angular_velocity = 15.0  # degrees/second for rotation simulation
        self.last_time = time.time()

    def read_accelerometer(self):
        # Simulate slight tilt on x-axis (pitch) with static z-gravity
        return {
            "x": math.sin(math.radians(self.angle)) * 9.81,
            "y": 0.0,
            "z": math.cos(math.radians(self.angle)) * 9.81
        }

    def read_gyroscope(self):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        # Simulate angular rate of change around x-axis (pitch)
        self.angle += self.angular_velocity * dt

        return {
            "x": self.angular_velocity,
            "y": 0.0,
            "z": 0.0
        }
