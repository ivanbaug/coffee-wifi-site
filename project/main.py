from flask import Flask, blueprints

CONFIG_FILE = "config.py"


def create_app(config_file=CONFIG_FILE):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # blueprint for non-auth parts of app
    from views import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, port=5000)
