import Adafruit_DHT

from sensors.dht.DhtType import DhtType


class DhtSensor:
    type: DhtType
    pin: int

    def __init__(self, pin=4, type=DhtType.DHT11):
        self.pin = pin
        self.type = type

    def get_temp(self) -> object:
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(self.type.value, self.pin)

        # Un-comment the line below to convert the temperature to Fahrenheit.
        # temperature = temperature * 9/5.0 + 32

        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).
        # If this happens try again!
        return {
            "temp": temperature,
            "hum": humidity
        }
