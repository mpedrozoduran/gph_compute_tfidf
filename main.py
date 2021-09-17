from flask import Flask
from blueprints.compute_endpoint import compute_blueprint
from blueprints.swagger import swaggerui_blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(compute_blueprint)
    flask_app.register_blueprint(swaggerui_blueprint)
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run()
