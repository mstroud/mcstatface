from app import app

from mcstatus import MinecraftServer

class StatusModel(object):
    server = MinecraftServer.lookup(app.config['MCSTATUS_URL'])
    status = server.status()
    