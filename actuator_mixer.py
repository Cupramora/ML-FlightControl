# actuator_mixer.py
# mixes PID outputs into motor thrust signals for quadcopter control

class ActuatorMixer:
    """
    Maps pitch, roll, yaw, and altitude corrections into motor outputs.
    Assumes X-configuration quad layout:
        Front
         ^
      1     2
         +
      3     4
    """

    def __init__(self, base_thrust=0.6, output_limits=(0.0, 1.0)):
        self.base_thrust = base_thrust
        self.min_thrust, self.max_thrust = output_limits

    def mix(self, pitch, roll, yaw, altitude):
        """
        Returns a dict of motor signals after mixing control outputs.
        """
        # Combine altitude base thrust with PID corrections
        m1 = self.base_thrust + pitch + roll - yaw + altitude
        m2 = self.base_thrust + pitch - roll + yaw + altitude
        m3 = self.base_thrust - pitch + roll + yaw + altitude
        m4 = self.base_thrust - pitch - roll - yaw + altitude

        return {
            "motor_1": self._clamp(m1),
            "motor_2": self._clamp(m2),
            "motor_3": self._clamp(m3),
            "motor_4": self._clamp(m4)
        }

    def _clamp(self, value):
        return max(self.min_thrust, min(self.max_thrust, round(value, 4)))
