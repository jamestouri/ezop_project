`python AthleteModel.py db init`
creates the migration of the table to the database

`python AthleteModel.py db migrate`
migrates table to database

`python AthleteModel.py db upgrade`

`docker-compose run web python /code/AthleteModel.py db init`
`docker-compose run web python /code/AthleteModel.py db migrate`
`docker-compose run web python /code/AthleteModel.py db upgrade`


`docker-compose run web python /ezop_project/src/models/AthleteModel.py db init`
