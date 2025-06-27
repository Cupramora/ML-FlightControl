# motor_bridge.py
# sends motor thrust signals to Electric Variation Control system

import json
import serial  # or socket, depending on your hardware bridge

class MotorBridge:
    """
    Translates motor outputs into serial commands for the electric controller.
    """

    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def send(self, motor_signals):
        """
        Sends motor thrust values as a JSON packet over serial.
        """
        packet = {
            "motor_1": motor_signals["motor_1"],
            "motor_2": motor_signals["motor_2"],
            "motor_3": motor_signals["motor_3"],
            "motor_4": motor_signals["motor_4"]
        }
        encoded = json.dumps(packet).encode("utf-8")
        self.ser.write(encoded)
        self.ser.write(b"\n")  # newline as delimiter
