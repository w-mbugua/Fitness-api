from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.users import UserModels
from flask_restful.reqparse import RequestParser
from app.utilities.validator import Validators
from werkzeug.security import generate_password_hash, check_password_hash

validate = Validators()


class User(Resource):
    """class to handle single user access, updates and deleting"""
    def get(self, user_id):
        user = UserModels.fetch_user_by_userid(user_id)
        if not user:
            return { "message": "user not found"}, 404
        return user

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass


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

    def post(self):
        """register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        email = args['email']
        password = args['password']
        confirm_password = args['confirm_password']

        if not validate.password_confirm(password, confirm_password):
            return {
                "status": 400,
                "message": "Please confirm your password"
            }, 400
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
        results = new_user
        results.password = validate.hash_password(password)
        results. confirm_password = validate.hash_password(confirm_password)
        return {
            "status": 201,
            "message": "user registered",
            "user": results.__dict__
        }, 201

    #put

    #delete

class AllUsers(Resource):
    # get users
    def get(self):
        """get all user endpoints"""
        users = UserModels.fetch_all(self)
        if users:
            return {
                       "status": "Ok",
                       "users": users}, 200
        else:
            return {
                       "message": "No user found"}, 404

class LoginManager(Resource):
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

    def post(self):
        """register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        email = args['email']
        password = args['password']

        user = UserModels.fetch_user_by_email(email)
        if not user or password != user['password']:
            return {
                "status": 400,
                "message": "Wrong login credentials"
            }
        return {
            "status": 201,
            "message": "Login successful"
        }


