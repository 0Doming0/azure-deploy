from flask import Flask, render_template, request
from flask_socketio import SocketIO
from routes import api
import time
from calculate import somar

app = Flask(__name__)
socket = SocketIO(app)

app.register_blueprint(api)

data = {}

@app.route("/")
def home():
    
    return render_template("/home.html")

@app.route("/now")
def now():
    if data == {}:  
      return time.strftime("%H:%M")
    return data

@app.route("/receive", methods=["POST"])
def receive_():
    data = request.json
    return request.json

# if __name__ == '__main__':
#   app.run("0.0.0.0")
