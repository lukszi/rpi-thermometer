from datetime import datetime

from information_provider.BaseInformationProvider import BaseInformationProvider
import requests
from requests.auth import HTTPDigestAuth


class RESTInformationProvider(BaseInformationProvider):
    """Provides Information from a provided REST-api"""
    def get_current_data(self, item):
        param = dict()
        if self.sensor is not None:
            param["sensor"] = self.sensor
        if self.user is not None and self.auth is not None:
            resp = requests.get(url=self.base_path, params=param, auth=HTTPDigestAuth(self.user, self.auth))
        else:
            resp = requests.get(self.base_path)
        return {"data": resp.json()[item],
                "timeStamp": datetime.utcnow(),
                "item": item}

    def __init__(self, base_path, user=None, auth=None, sensor=None):
        """Basepath:"""
        super(RESTInformationProvider).__init__()
        self.base_path = base_path
        self.user = user
        self.auth = auth
        self.sensor = sensor
