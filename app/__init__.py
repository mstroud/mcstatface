from flask import Flask

app = Flask(__name__)
app.config['MCSTATUS_URL'] = "alsochris.com:25565"

from app import views
from app import models
