import os
from flask import Blueprint, redirect, render_template, request, url_for, flash

from .models import Cafe

# from . import db

INFO_EMAIL = os.environ.get("INFO_EMAIL")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=cafes)
