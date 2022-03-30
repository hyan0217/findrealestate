from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
