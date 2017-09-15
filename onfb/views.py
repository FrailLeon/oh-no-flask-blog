#coding: utf8
from . import app
from . import request, render_template

@app.route('/')
def index():
    return render_template('index.html')