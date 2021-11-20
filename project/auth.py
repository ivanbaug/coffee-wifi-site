from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for, render_template, Blueprint, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from . import db
from .models import User
from .forms import LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # find user by email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("get_all_posts"))
            else:
                flash("Wrong password or user, please try again.")
                return redirect(url_for("login"))
        else:
            flash("Wrong user or password, please try again.")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)
