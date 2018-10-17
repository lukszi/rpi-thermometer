from abc import ABCMeta, abstractmethod
from database import DB


class BaseInformationProvider(object):
    __metaclass__ = ABCMeta

    def __init__(self, database: DB = None):
        self.db = database

    def __getitem__(self, item):
        try:
            return self.get_data(item)
        except KeyError:
            return False

    def get_data(self, item, start=None, end=None):
        if start == end:
            # No parameters were set, get current data
            if start is None or end is None:
                return self.get_current_data(item)
            # Parameters were set, get data from database
            else:
                if self.db is None:
                    raise AttributeError("can't get historical data, No database passed to constructor")
                return self.db.get_data_points(item, start, end)

    @abstractmethod
    def get_current_data(self, item):
        pass
