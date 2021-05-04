from flask import jsonify, make_response , request
from flask_restful import Resource

from app.auth.v1.model.user_model import UserModels

class Users(Resource):
    """ Class to register user(s) """

    def get(self):
        return {'hello': world} , 200