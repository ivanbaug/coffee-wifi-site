from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy

CONFIG_FILE = "config.py"

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app(config_file=CONFIG_FILE):

    # Setup app
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    # Import db models
    from .models import User
    from .models import Cafe
    from .models import Comment

    ### 2 Lines below only required once, when creating DB. ####
    with app.app_context():
        db.create_all()

    # blueprint for non-auth parts of app
    from .views import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app


app = create_app()
