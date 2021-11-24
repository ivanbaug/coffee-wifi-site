from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    IntegerField,
    BooleanField,
    SelectField,
)
from wtforms.validators import DataRequired, Email, URL, EqualTo, InputRequired
from wtforms.fields import DecimalField, EmailField


class NewUserForm(FlaskForm):
    name = StringField("Your Name:", validators=[DataRequired()])
    email = EmailField(
        "Your email:",
        validators=[DataRequired(), Email("This field requires a valid email address")],
    )
    password = PasswordField(
        "Password:",
        validators=[
            InputRequired(),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up!")


class LoginForm(FlaskForm):
    email = EmailField(
        "Your email:",
        validators=[DataRequired(), Email("This field requires a valid email address")],
    )
    password = PasswordField("Password:", validators=[InputRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log In")


class NewCafeForm(FlaskForm):
    name = StringField("New cafe name:", validators=[DataRequired()])
    map_url = StringField("Google maps url:", validators=[DataRequired()])
    img_url = StringField("Url of a picture of the site:", validators=[DataRequired()])
    location = StringField("Address:", validators=[DataRequired()])
    seats = StringField("Number of seats (aprox.):", validators=[DataRequired()])
    has_toilet = BooleanField("Has toilets?")
    has_wifi = BooleanField("Has wifi?")
    has_sockets = BooleanField("Has sockets?")
    can_take_calls = BooleanField("Can you take calls there?")
    coffee_price = StringField("Coffee cup price (optional):")
    submit = SubmitField("Add Cafe")


# TODO: New comment form
