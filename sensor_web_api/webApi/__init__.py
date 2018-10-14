from flask import Flask
from flask_restful import Resource, Api
# from information_provider import BME280InformationProvider
from information_provider import DummyInformationProvider
from util import Config
from database import DB

app = Flask(__name__)
api = Api(app)


class TemperatureProvider(Resource):
    def get(self):
        conf = Config("config.ini")
        database_conf = conf["database"]
        db = DB(database_conf["server"], database_conf["user"], database_conf["password"])
        sensor = DummyInformationProvider(db)
        return{
            "humidity": sensor["humidity"]["data"],
            "pressure": sensor["pressure"]["data"],
            "temperature": sensor["temperature"]["data"]
        }


api.add_resource(TemperatureProvider, '/')
