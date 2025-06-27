# sensor_bridge.py
# connects to ML-SensorHub and streams real-time sensor data into the flight loop

class SensorBridge:
    """
    Interfaces with ML-SensorHub to retrieve real-time sensor data.
    """

    def __init__(self, sensorhub_client):
        self.client = sensorhub_client

    def get_sensor_data(self):
        """
        Returns a unified sensor data dict for use in control loops.
        """
        imu = self.client.get_imu()           # accel + gyro
        gps = self.client.get_gps()           # lat, lon, alt
        baro = self.client.get_barometer()    # altitude

        return {
            "accelerometer": imu["accel"],
            "gyroscope": imu["gyro"],
            "gps": gps,
            "barometer": baro
        }
