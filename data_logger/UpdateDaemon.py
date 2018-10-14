from threading import Thread
from time import sleep

from information_provider import BaseInformationProvider
from database import DB


class UpdateDaemon(Thread):
    def __init__(self, db: DB, information_provider: BaseInformationProvider, polling_interval, items):
        Thread.__init__(self)
        self.db = db
        self.information_provider = information_provider
        self.polling_interval = polling_interval
        self.items = items
        print("created")

    def run(self):
        print("running")
        while True:
            self.db.connect()
            data_list = []
            # print("getting data")
            for item in self.items:
                # print("\t\t" + item)
                data_list.append(self.information_provider.get_current_data(item))
            # print("writing into db")
            for data in data_list:
                self.db.write_data_point(data["item"], data["data"], data["timeStamp"])
            self.db.disconnect()
            sleep(self.polling_interval)
