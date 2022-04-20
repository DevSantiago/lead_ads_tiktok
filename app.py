from flask import Flask
from flask import request, redirect, url_for
import requests
import json

app = Flask(__name__)


@app.route("/")
def main():
    return "<p>Hola!</p>"


if __name__ == "__main__":
    app.run(debug=True)