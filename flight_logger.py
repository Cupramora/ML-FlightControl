# flight_logger.py
# logs flight state, PID outputs, and sensor data over time

import csv
import time
import os

class FlightLogger:
    """
    Logs flight telemetry and control outputs to CSV for analysis.
    """

    def __init__(self, filename="logs/flight_log.csv"):
        self.filename = filename
        self._ensure_header()

    def _ensure_header(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", "pitch", "roll", "yaw", "altitude",
                    "motor_1", "motor_2", "motor_3", "motor_4"
                ])

    def log(self, state):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                round(time.time(), 3),
                state["attitude"]["pitch"],
                state["attitude"]["roll"],
                state["attitude"]["yaw"],
                state["altitude"],
                state["motors"]["motor_1"],
                state["motors"]["motor_2"],
                state["motors"]["motor_3"],
                state["motors"]["motor_4"]
            ])
