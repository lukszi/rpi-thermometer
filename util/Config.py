import configparser
import json


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def __call__(self, *kargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated(*kargs)
            return self._instance

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Config(object):
    _config = None

    def __init__(self, config_path=None):
        print("Init called with path: " + config_path)
        self._config = configparser.ConfigParser()
        self._config.read(config_path)

    def __getitem__(self, item):
        return self._config[item]


if __name__ == "__main__":
    conf1 = Config("config.ini")
    conf2 = Config()
    print(conf1["database"]["server"])
    print(json.loads(conf1["daemon"]["item_list"]))
