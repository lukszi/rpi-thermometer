from datetime import datetime
import board
import busio
import adafruit_bme280

from information_provider.BaseInformationProvider import BaseInformationProvider
from database import DB


class BME280InformationProvider(BaseInformationProvider):
    def __init__(self, database: DB):
        super(BME280InformationProvider, self).__init__(database)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        adafruit_bme280._BME280_ADDRESS = 76
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c)

    def get_current_data(self, item):
        return {
            "dataPoint": getattr(self.bme280, item),
            "timeStamp": datetime.utcnow(),
            "item": item}
