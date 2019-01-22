from threading import Thread
from time import sleep
import sys

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
            try:
                self.db.connect()
            except:
                print("Error while trying to connect to database", file=sys.stderr)
                continue

            data_list = []
            # print("getting data")
            try:
                for item in self.items:
                    # print("\t\t" + item)
                    data_list.append(self.information_provider.get_current_data(item))
                # print("writing into db")
            except:
                print("Error while trying to get data", file=sys.stderr)
                continue

            try:
                for data in data_list:
                    self.db.write_data_point(data["item"], data["data"], data["timeStamp"])
            except:
                print("Error while writing into database", file=sys.stderr)
                continue

            try:
                self.db.disconnect()
            except:
                print("Error while trying to disconnect from database", file=sys.stderr)
                continue

            sleep(int(self.polling_interval))
