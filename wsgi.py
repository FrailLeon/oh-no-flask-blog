#coding: utf8

from onfb import app

app.debug = True

if __name__ == '__main__':
    app.run('0.0.0.0')
else:
    application = app
