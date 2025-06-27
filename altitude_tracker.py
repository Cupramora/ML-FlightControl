# altitude_tracker.py
# fuses barometer and GPS data to estimate current altitude

class AltitudeTracker:
    """
    Combines barometric pressure and GPS altitude to estimate vertical position.
    Uses a weighted average with optional smoothing.
    """

    def __init__(self, barometer, gps, alpha=0.85):
        self.barometer = barometer
        self.gps = gps
        self.alpha = alpha  # weight for barometer vs GPS
        self.estimated_altitude = 0.0
        self.initialized = False

    def update(self):
        baro_alt = self.barometer.get_altitude()  # meters
        gps_alt = self.gps.get_altitude()         # meters

        if not self.initialized:
            self.estimated_altitude = (baro_alt + gps_alt) / 2
            self.initialized = True
        else:
            self.estimated_altitude = (
                self.alpha * baro_alt +
                (1 - self.alpha) * gps_alt
            )

        return round(self.estimated_altitude, 3)

    def get_altitude(self):
        return self.estimated_altitude
