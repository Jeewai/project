from marshmallow import Schema, fields


class PlainTaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)
    assigned = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str()
    due_date = fields.DateTime()
    is_urgent = fields.Bool()


class PlainProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str()


class TaskSchema(PlainTaskSchema):
    project_id = fields.Int(required=True, load_only=True)
    project = fields.Nested(PlainProjectSchema(), dump_only=True)


class TaskUpdateSchema(Schema):
    name = fields.Str()
    status = fields.Str()
    assigned = fields.Str()
    category = fields.Str()
    description = fields.Str()
    due_date = fields.DateTime()
    is_urgent = fields.Bool()


class ProjectSchema(PlainProjectSchema):
    tasks = fields.List(fields.Nested(PlainTaskSchema()), dump_only=True)