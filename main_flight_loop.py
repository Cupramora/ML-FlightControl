# main_flight_loop.py
# runs the real-time flight stabilization loop using sensor input and PID control

import time
from pid_initializer import initialize_pid_system
from command_listener import CommandListener
from feedback_stream import FeedbackStream
from flight_logger import FlightLogger
from sensors.barometer import Barometer
from sensors.gps import GPS
from altitude_tracker import AltitudeTracker

# Initialize core components
components = initialize_pid_system()
loop_hub = components["loop_hub"]
tracker = components["orientation_tracker"]
mixer = components["actuator_mixer"]

command = CommandListener()
feedback = FeedbackStream(log_file="logs/flight_log.csv")
logger = FlightLogger()

# Initialize altitude tracker
barometer = Barometer()
gps = GPS()
alt_tracker = AltitudeTracker(barometer, gps)

# Main loop parameters
frequency = 50  # Hz
dt = 1.0 / frequency

print("🛫 Flight loop initialized. Stabilizing...")

while True:
    # 1. Read sensors
    attitude = tracker.get_orientation()
    current_altitude = alt_tracker.update()
    target = command.get_target()

    # 2. Build sensor package for loop hub
    sensor_data = {
        "attitude": attitude,
        "altitude": current_altitude,
        "target": target
    }

    # 3. Update all control loops
    corrections = loop_hub.update_all(sensor_data, dt)

    # 4. Mix corrections into motor commands
    motor_signals = mixer.mix(
        pitch=corrections["pitch"],
        roll=corrections["roll"],
        yaw=corrections["yaw"],
        altitude=corrections["altitude"]
    )

    # 5. State packet
    state = {
        "attitude": attitude,
        "altitude": current_altitude,
        "gps": gps.get_position(),
        "motors": motor_signals
    }

    # 6. Feedback and log
    feedback.send(state)
    logger.log(state)

    time.sleep(dt)