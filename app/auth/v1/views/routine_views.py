from flask import  jsonify, make_response, request
from flask_restful import Resource

from app.auth.v1.model.routine import routinemodels

class Routine(Resource):
    """class to register routine"""

    def get(self):
        return{'hello'},200

