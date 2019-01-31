from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .AthleteModel import AthleteModel, AthleteSchema
