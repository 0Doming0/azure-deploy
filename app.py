from flask import Flask, render_template, request
from flask_socketio import SocketIO
from routes import api
import time
from calculate import somar

app = Flask(__name__)
socket = SocketIO(app)

app.register_blueprint(api)

data = {}

data_app = {}

@app.route("/")
def home():
    
    return render_template("/home.html")

@app.route("/now")
def now():
    if data_app == {}:
      return time.strftime("%H:%M")
    return data_app["message"]

@app.route("/receive", methods=["POST"])
def receive_():
    data = request.get_json()
    if data and 'id' in data:
       data_app["message"] = data  
       return '', 200
    return '', 403

data_app = {}
if __name__ == '__main__':
  app.run("0.0.0.0")