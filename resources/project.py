from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ProjectModel
from schemas import ProjectSchema

blp = Blueprint("Projects", __name__, description="Operations on projects")

@blp.route("/project/<string:project_id>")
class Project(MethodView):
    @blp.response(200, ProjectSchema)
    def get(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)
        return project

    def delete(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return {"message": "Project deleted."}


@blp.route("/project")
class ProjectList(MethodView):
    @blp.response(200, ProjectSchema(many=True))
    def get(self):
        return ProjectModel.query.all()
    
    @blp.arguments(ProjectSchema)
    @blp.response(200, ProjectSchema)
    def post(self, project_data):
        print(project_data)
        
        project = ProjectModel(**project_data)
        try:
            db.session.add(project)
            db.session.commit
        except IntegrityError:
            abort(400, message="A project with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occured creating the project.")

        return project