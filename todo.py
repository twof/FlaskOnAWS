from main import db
from sqlalchemy.dialects.postgresql import JSON


class Todo(db.Model):
    __tablename__ = 'global_todo'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }