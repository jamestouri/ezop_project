from marshmallow import (
    fields,
    Schema,
)
import datetime

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/challenge'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class AthleteModel(db.Model):
    __tablename__ = 'athletes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140), nullable=False)
    sport = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)


    def __init__(self, data):
        self.name = data.get('name')
        self.sport = data.get('sport')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_athletes():
        return AthleteModel.query.all()

    @staticmethod
    def get_one_athlete(id):
        return AthleteModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class AthleteSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    sport = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

if __name__ == '__main__':
    manager.run()
