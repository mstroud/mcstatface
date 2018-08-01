from app import app

from mcstatus import MinecraftServer

class StatusModel(object):
    def __init__(self,urlstr=None):
        if urlstr:
            self.server = MinecraftServer.lookup(urlstr)
        else:
            self.server = MinecraftServer.lookup(app.config['MCSTATUS_URL'])
        self.status = self.server.status()
    