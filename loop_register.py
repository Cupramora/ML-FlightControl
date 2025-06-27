# loop_register.py
# dynamic registry of active control loops

class LoopRegister:
    """
    Holds and manages all active control loops (e.g. pitch, roll, yaw, altitude).
    """

    def __init__(self):
        self.loops = {}

    def register(self, name, loop_instance):
        self.loops[name] = loop_instance

    def unregister(self, name):
        if name in self.loops:
            del self.loops[name]

    def get_loops(self):
        return self.loops

    def list_active(self):
        return list(self.loops.keys())
