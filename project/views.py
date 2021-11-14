import os
from flask import Blueprint, redirect, render_template, request, url_for, flash

INFO_EMAIL = os.environ.get("INFO_EMAIL")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")
