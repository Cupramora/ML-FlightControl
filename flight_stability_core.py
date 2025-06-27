# flight_stability_core.py

import time
from sensors.imu import IMU
from sensors.gps import GPS
from sensors.barometer import Barometer
from flight_controller.pid_controller import PID
from flight_controller.orientation_tracker import OrientationTracker
from flight_controller.actuator_mixer import ActuatorMixer

class FlightStabilityCore:
    """
    Central PID loop that fuses sensor data and outputs motor corrections.
    """

    def __init__(self, target_attitude={"pitch": 0.0, "roll": 0.0, "yaw": 0.0, "altitude": 1.5}):
        self.imu = IMU()
        self.gps = GPS()
        self.barometer = Barometer()
        self.tracker = OrientationTracker(self.imu)
        self.mixer = ActuatorMixer()

        self.target = target_attitude

        self.pid_pitch = PID(kp=1.2, ki=0.01, kd=0.05)
        self.pid_roll  = PID(kp=1.2, ki=0.01, kd=0.05)
        self.pid_yaw   = PID(kp=0.8, ki=0.005, kd=0.02)
        self.pid_alt   = PID(kp=1.0, ki=0.02, kd=0.1)

    def update(self, dt):
        # 1. Sensor fusion
        attitude = self.tracker.get_orientation()  # pitch, roll, yaw
        altitude = self.barometer.get_altitude()
        gps_fix = self.gps.get_position()

        # 2. PID corrections
        pitch_out = self.pid_pitch.compute(self.target["pitch"], attitude["pitch"], dt)
        roll_out  = self.pid_roll.compute(self.target["roll"], attitude["roll"], dt)
        yaw_out   = self.pid_yaw.compute(self.target["yaw"], attitude["yaw"], dt)
        alt_out   = self.pid_alt.compute(self.target["altitude"], altitude, dt)

        # 3. Motor mixing
        motor_signals = self.mixer.mix(pitch_out, roll_out, yaw_out, alt_out)

        return {
            "motors": motor_signals,
            "attitude": attitude,
            "altitude": altitude,
            "gps": gps_fix
        }
