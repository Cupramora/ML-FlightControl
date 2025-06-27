# feedback_stream.py
# sends telemetry and control state to PerceptionCore or logging systems

import time

class FeedbackStream:
    """
    Streams flight state, control outputs, and sensor readings to PerceptionCore or logs.
    """

    def __init__(self, perception_callback=None, log_file=None):
        self.perception_callback = perception_callback
        self.log_file = log_file

    def send(self, state):
        """
        Sends a snapshot of the current flight state.
        """
        packet = {
            "timestamp": time.time(),
            "attitude": state.get("attitude"),
            "altitude": state.get("altitude"),
            "gps": state.get("gps"),
            "motor_signals": state.get("motors")
        }

        if self.perception_callback:
            self.perception_callback(packet)

        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(str(packet) + "\n")
