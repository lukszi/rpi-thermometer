from datetime import datetime
import board
import busio
from adafruit_bme280 import Adafruit_BME280_I2C

from information_provider.BaseInformationProvider import BaseInformationProvider
from database import DB


class BME280InformationProvider(BaseInformationProvider):
    def __init__(self, database: DB):
        super(BME280InformationProvider, self).__init__(database)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bme280 = Adafruit_BME280_I2C(self.i2c, address=0x76)

    def get_current_data(self, item):
        return {
            "data": getattr(self.bme280, item),
            "timeStamp": datetime.utcnow(),
            "item": item}
