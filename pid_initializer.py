# pid_initializer.py
# initializes and connects all PID control loops and core flight modules

from flight_controller.pid_controller import PID
from flight_controller.orientation_tracker import OrientationTracker
from flight_controller.actuator_mixer import ActuatorMixer
from loop_register import LoopRegister
from loop_hub import LoopHub
from sensors.imu import IMU

def initialize_pid_system():
    """
    Sets up all PID loops, orientation tracking, and actuator mixer.
    Returns the loop hub, orientation tracker, and actuator mixer.
    """
    imu = IMU()
    tracker = OrientationTracker(imu)
    mixer = ActuatorMixer()
    register = LoopRegister()

    # Register PID loops
    register.register("pitch", PID(kp=1.2, ki=0.01, kd=0.05))
    register.register("roll",  PID(kp=1.2, ki=0.01, kd=0.05))
    register.register("yaw",   PID(kp=0.8, ki=0.005, kd=0.02))
    register.register("altitude", PID(kp=1.0, ki=0.02, kd=0.1))

    hub = LoopHub(register)

    return {
        "loop_hub": hub,
        "orientation_tracker": tracker,
        "actuator_mixer": mixer
    }
