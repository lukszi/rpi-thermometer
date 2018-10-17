import json

from data_logger.UpdateDaemon import UpdateDaemon
from database import DB
from information_provider.DummyInformationProvider import DummyInformationProvider
from information_provider.RESTInformationProvider import RESTInformationProvider
from util import Config

if __name__ == '__main__':
    conf = Config("config.ini")
    database_conf = conf["database"]
    daemon_conf = conf["daemon"]
    db = DB(database_conf["server"], database_conf["user"], database_conf["password"])
    daemon = UpdateDaemon(db, RESTInformationProvider("http://msu.oph.rwth-aachen.de/"), daemon_conf["polling_interval"],
                          json.loads(daemon_conf["item_list"]))
    daemon.run()
