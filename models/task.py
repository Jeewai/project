from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    status = db.Column(db.String(20), unique=False, nullable=False)
    assigned = db.Column(db.String(80), unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    due_date = db.Column(db.DateTime, unique=False, nullable=True)
    is_urgent = db.Column(db.Boolean, unique=False, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), unique=False, nullable=False)
    
    project = db.relationship("ProjectModel", back_populates="tasks")
