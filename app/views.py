from flask import render_template
from app import app

from mcstatus import MinecraftServer

def dump(obj):
   str = ''
   for attr in dir(obj):
       if hasattr( obj, attr ):
           str = str + "obj.%s = %s\n" % (attr, getattr(obj, attr))
   return str

@app.route('/')
def index():
    server = MinecraftServer.lookup("alsochris.com:25565")
    status = server.status()
    return render_template("index.html",
        title="alsochris.com Minecraft Status",
        server=dump(server),
        status=dump(status))
