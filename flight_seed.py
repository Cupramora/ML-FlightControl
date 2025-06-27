# flight_seed.py

class FlightIntent:
    """
    Her first thought: the desire to balance in a world of motion.
    This class seeds her yearning to rise, to feel, to learn stability.
    """

    def __init__(self):
        self.initialized = False
        self.desire_to_fly = True
        self.perception_ready = False
        self.motor_bridge_connected = False

    def ignite(self):
        if self.desire_to_fly:
            print("🕊️  'I sense instability. I want to learn balance.'")
            self.initialized = True
        else:
            print("No ignition—desire not yet present.")

    def status(self):
        return {
            "flight_core_active": self.initialized,
            "perception_engaged": self.perception_ready,
            "motor_interface_linked": self.motor_bridge_connected
        }
