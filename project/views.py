import os
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

from project.forms import NewCafeForm
from .models import Cafe

# from . import db

INFO_EMAIL = os.environ.get("INFO_EMAIL")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=cafes)


@login_required
@main.route("/add-cafe", methods=["GET", "POST"])
def new_cafe():
    form = NewCafeForm()
    if form.validate_on_submit():
        print("hi")

    return render_template("new_cafe.html", form=form)
