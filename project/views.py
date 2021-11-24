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
from datetime import date
from project.forms import NewCafeForm
from .models import Cafe
from . import db

INFO_EMAIL = os.environ.get("INFO_EMAIL")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=cafes)


@main.route("/add-cafe", methods=["GET", "POST"])
@login_required
def new_cafe():
    form = NewCafeForm()
    if form.validate_on_submit():
        n_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            can_take_calls=form.can_take_calls.data,
            coffee_price=form.coffee_price.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(n_cafe)
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("new_cafe.html", form=form)


@main.route("/my-cafes", methods=["GET", "POST"])
@login_required
def my_cafes():
    cafes = Cafe.query.filter_by(author=current_user.name)
    return render_template("index.html", all_cafes=cafes)


@main.route("/delete/<int:cafe_id>")
@login_required
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    # if its the author or admin delete
    if (cafe_to_delete.author_id == current_user.id) or (current_user.id == 1):
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        # Send flash messsage
        flash("You have to be the author of the entry or admin to delete it.")
    return redirect(url_for("main.index"))
