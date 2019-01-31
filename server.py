from flask import Flask,render_template, request,jsonify,Response
from sqlalchemy import create_engine

from flask_script import Manager
from flask_migrate import Migrate

from src.models.AthleteModel import *

engine = create_engine('postgresql://postgres:postgres@localhost:5432/challenge')
# conn = engine.connect()

# # Testing migration on sqlite db
# engine = create_engine('sqlite:///ezop.sqlite', echo=False)
conn = engine.connect()


#Create the app object that will route our calls
app = Flask(__name__)


# Add a single endpoint that we can use for testing
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


#When run from command line, start the server
if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug = True)
