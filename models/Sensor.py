from models.SensorInterface import SensorInterface
from models.SensorType import SensorType
from models.SensorUnit import SensorUnit


class Sensor:
    id: int
    type: SensorType = SensorType.RELAY
    unit: SensorUnit = SensorUnit.CONVENTIONAL_UNITS
    value: str
    time: int
    interface: SensorInterface
