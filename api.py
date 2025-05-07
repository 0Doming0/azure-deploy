from flask import Blueprint, redirect

api = Blueprint("api", __name__)

@api.route("/redirect")
def redirect():
    return redirect('/now')