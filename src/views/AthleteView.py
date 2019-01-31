from flask import (
    request,
    g,
    Blueprint,
    json,
    Response,
)
from ..models.AthleteModel import(
    AthleteModel,
    AthleteSchema,
)


athlete_api = Blueprint('athlete_api', __name__)
athlete_schema = AthleteSchema()


def  response(res, status_code):
  """Custom Response"""
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
  
@comment_api.route('/', methods=['POST'])
def create():
    """Creating Comment"""
    req_data = request.get_json()

    data, error = comment_schema.load(req_data)
    if error:
        return response(error, 400)
    comment = CommentModel(data)
    comment.save()
    data = comment_schema.dump(comment).data
    return response(data, 201)
