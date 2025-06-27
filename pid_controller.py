# pid_controller.py

import time

class PID:
    """
    A reusable PID controller for flight stabilization and control loops.
    """

    def __init__(self, kp=1.0, ki=0.0, kd=0.0, output_limits=(-1.0, 1.0)):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_time = time.time()

        self.output_min, self.output_max = output_limits

    def compute(self, setpoint, measurement, dt=None):
        now = time.time()
        if dt is None:
            dt = now - self.prev_time
            self.prev_time = now

        error = setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0

        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )

        output = max(self.output_min, min(self.output_max, output))
        self.prev_error = error
        return output

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_time = time.time()
