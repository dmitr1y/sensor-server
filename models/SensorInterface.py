from enum import Enum


class SensorInterface(Enum):
    SPI = "spi"
    I2C = "i2c"
    ANALOG = "analog"
