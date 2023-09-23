from flask import Flask
from flask_smorest import Api
import models, os

from db import db

# from resources.partner import blp as PartnerBlueprint
from resources.project import blp as ProjectBlueprint
from resources.task import blp as TaskBlueprint
# from resources.team import blp as TeamBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "postgresql://postgres:django1234@localhost/project2_flask")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    # api.register_blueprint(PartnerBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(TaskBlueprint)
    # api.register_blueprint(TeamBlueprint)

    return app