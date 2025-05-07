from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)

@app.route("/")
def home():
    return render_template("/home.html")

# if __name__ == '__main__':
#   app.run("0.0.0.0")