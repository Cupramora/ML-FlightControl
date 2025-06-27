# orientation_tracker.py

import math
import time

class OrientationTracker:
    """
    Fuses accelerometer and gyroscope data into pitch, roll, and yaw estimates.
    Uses a complementary filter for stability.
    """

    def __init__(self, imu, alpha=0.98):
        self.imu = imu
        self.alpha = alpha  # Complementary filter weight
        self.pitch = 0.0
        self.roll = 0.0
        self.yaw = 0.0
        self.last_time = time.time()

    def get_orientation(self):
        accel = self.imu.read_accelerometer()  # dict: x, y, z
        gyro = self.imu.read_gyroscope()       # dict: x, y, z
        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        # Accelerometer angle estimates
        accel_pitch = math.atan2(accel["y"], accel["z"]) * 180 / math.pi
        accel_roll  = math.atan2(-accel["x"], accel["z"]) * 180 / math.pi

        # Integrate gyro rates
        self.pitch += gyro["x"] * dt
        self.roll  += gyro["y"] * dt
        self.yaw   += gyro["z"] * dt

        # Complementary filter
        self.pitch = self.alpha * self.pitch + (1 - self.alpha) * accel_pitch
        self.roll  = self.alpha * self.roll  + (1 - self.alpha) * accel_roll

        return {
            "pitch": round(self.pitch, 3),
            "roll": round(self.roll, 3),
            "yaw": round(self.yaw, 3)
        }
