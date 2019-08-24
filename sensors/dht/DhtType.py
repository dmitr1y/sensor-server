from enum import Enum

import Adafruit_DHT


class DhtType(Enum):
    DHT11 = Adafruit_DHT.DHT11
    DHT22 = Adafruit_DHT.DHT22
    DHT2302 = Adafruit_DHT.AM2302
