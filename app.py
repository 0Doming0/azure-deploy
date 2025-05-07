from flask import Flask
import socketio

app = Flask(__name__)

@app.route("/")
def home():
    return "BEM-VINDO A SUA PÁGINA"

if __name__ == '__main__':
  app.run("0.0.0.0")