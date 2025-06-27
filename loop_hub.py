# loop_hub.py
# orchestrates all active PID loops

class LoopHub:
    """
    Central coordinator for all active PID loops.
    Routes sensor data to each loop and collects control outputs.
    """

    def __init__(self, loop_register):
        self.registry = loop_register

    def update_all(self, sensor_data, dt):
        """
        Updates all registered loops with current sensor data and returns control outputs.
        """
        outputs = {}
        for name, loop in self.registry.get_loops().items():
            outputs[name] = loop.update(sensor_data, dt)
        return outputs
