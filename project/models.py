from flask_login import UserMixin
from sqlalchemy.orm import relationship
from . import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # User has a parent relationship with respect to Comments and Cafe
    # This will act like a List of Cafe objects attached to each User.
    # The "author" refers to the author property in the Cafe class.
    usites = relationship("Cafe", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


# Cafe TABLE Configuration
class Cafe(db.Model):
    __tablename__ = "cafes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=False)
    #  Cafe is child of user
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="usites")

    # Cafe has a parent relationship with respect to Comments
    comments = relationship("Comment", back_populates="parent_cafe")

    def to_dict(self):

        # Method 1.
        mydict = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            mydict[column.name] = getattr(self, column.name)
        return mydict

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    com_date = db.Column(db.String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    comment_author = relationship("User", back_populates="comments")

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    cafe_id = db.Column(db.Integer, db.ForeignKey("cafes.id"))
    # Create reference to the User object, the "cafes" refers to the cafes property in the User class.
    parent_cafe = relationship("Cafe", back_populates="comments")
