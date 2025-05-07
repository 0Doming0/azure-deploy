from flask import Flask, render_template, request
from flask_socketio import SocketIO
from routes import api
import time
from calculate import somar

app = Flask(__name__)
socket = SocketIO(app)

app.register_blueprint(api)

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/now")
def now():
    return time.strftime("%H:%M")

@app.route("/receive", methods=["POST"])
def receive_():
    return request.json

# if __name__ == '__main__':
#   app.run("0.0.0.0")