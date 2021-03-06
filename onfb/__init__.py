#coding: utf8

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



db = SQLAlchemy()


@app.errorhandler(404)
def paged_not_found(err):
    return render_template('404.html')