from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.users import UserModels
from flask_restful.reqparse import RequestParser
from app.utilities.validator import Validators

validate = Validators()
class Users(Resource):
    """class for users endoints"""
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('email',
                                 type=str,
                                 required=True,
                                 help="Please input an email")
        self.parser.add_argument('password',
                                 type=str,
                                 required=True,
                                 help="Please enter a password")
        self.parser.add_argument('confirm_password',
                                 type=str,
                                 required=True,
                                 help="Kindly confirm your password")

    def get(self):
        """get all user endpoints"""
        users = UserModels.fetch_all(self)
        return {
            "users": users
        }

    # can i have another get for one user?

    def post(self):
        """register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        email = args['email']
        password = args['password']
        confirm_password = args['confirm_password']

        if not validate.valid_email(email):
            return {
                "status": 400,
                "error": "Kindly put a valid email"
            }

        if validate.user_exists(email):
            return {
                "status": 400,
                "error": "User already exists"
            }

        new_user = UserModels(email, password, confirm_password)
        new_user.register()
        return {
            "status": 201,
            "message": "user registered",
            "user": new_user.__dict__
        }, 201

