import pysftp
import sys

# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
class Sftp:
    trigger = ""
    objserver = None

    def __init__(self, dicproject,trigger):
        print("Sftp...")
        self.dicproject = dicproject
        self.trigger = trigger # backend, frontend, db
        pass

    def _backend(self):
        pass

    def connect(self):
        dicprod = self.dicproject[self.trigger]["prod"]
        host = dicprod["host"]
        user = dicprod["user"]
        password = dicprod["password"]
        path = dicprod["path"]

#home337670657.1and1-data.host
        # self.objserver = pysftp.Connection(host=host, username=user, password=password)
        
        print(self.objserver)




