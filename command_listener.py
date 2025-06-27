# command_listener.py
# receives target attitude or trajectory commands from external sources

class CommandListener:
    """
    Listens for incoming control commands (e.g. from ML-Command, joystick, or mission planner).
    """

    def __init__(self):
        self.target_attitude = {"pitch": 0.0, "roll": 0.0, "yaw": 0.0, "altitude": 1.5}

    def receive(self, command_packet):
        """
        Updates internal target attitude based on incoming command.
        """
        for key in self.target_attitude:
            if key in command_packet:
                self.target_attitude[key] = command_packet[key]

    def get_target(self):
        return self.target_attitude
