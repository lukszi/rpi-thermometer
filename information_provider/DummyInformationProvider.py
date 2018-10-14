from information_provider.BaseInformationProvider import BaseInformationProvider
import random
from _datetime import datetime
from database import DB


class DummyInformationProvider(BaseInformationProvider):
    def __init__(self, database: DB):
        super(DummyInformationProvider, self).__init__(database)

    def get_current_data(self, item):
        return {
            "data": random.randint(0, 20),
            "timeStamp": datetime.utcnow(),
            "item": item}
