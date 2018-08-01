from flask import render_template
from app import app
from app import models

@app.route('/')
def index():
    s = models.StatusModel()
    return render_template("index.html",s=s)
