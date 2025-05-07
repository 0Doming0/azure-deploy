from flask import Flask, render_template
from flask_socketio import SocketIO
from api import api
import time

app = Flask(__name__)
socket = SocketIO(app)

app.register_blueprint(api)

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/now")
def now():
    return time.strftime("%H:%M")

# if __name__ == '__main__':
#   app.run("0.0.0.0")