from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.users import UserModels
from flask_restful.reqparse import RequestParser
from app.utilities.validator import Validators
from werkzeug.security import generate_password_hash, check_password_hash

validate = Validators()

class RegistrationManager(Resource):
    """class for users endoints"""
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('first_name', type=str, required=True, help="Please enter the first name")
        self.parser.add_argument('last_name', type=str, required=True, help="Please enter the last name")
        self.parser.add_argument('age', type=int, required=True, help="Please enter age")
        self.parser.add_argument('email', type=str, required=True, help="Please input an email")
        self.parser.add_argument('password', type=str, required=True, help="Please enter a password")
        self.parser.add_argument('confirm_password', type=str, required=True, help="Kindly confirm your password")

    def post(self):
        """method to register a user"""
        args = self.parser.parse_args()
        args = request.get_json()
        first_name = args['first_name']
        last_name = args['last_name']
        age = args['age']
        email = args['email']
        password = args['password']
        confirm_password = args['confirm_password']

        if not validate.is_astring(first_name) or not validate.is_astring(last_name):
            return {"error": "PLease enter a valid name"}
        if len(first_name) < 3 or len(last_name) < 3:
            return {"message": "Name should have atleast three characters"}
        if not validate.password_confirm(password, confirm_password):
            return {"message": "Please confirm your password"}, 400
        if not validate.valid_email(email):
            return {"error": "Kindly put a valid email"}, 400

        if validate.user_exists(email):
            return {"error": "User already exists"}, 400

        new_user = UserModels(first_name, last_name, age, email, password, confirm_password)
        new_user.register()
        # passing the new user toa new variable so that we can returned a 'hashed' password
        results = new_user
        results.password = validate.hash_password(password)
        results.confirm_password = validate.hash_password(confirm_password)
        return {
                   "message": "User has been registered",
                   "results": len(UserModels.users),
                   "user": results.__dict__
               }, 201

class Users(Resource):
    # get all users
    def get(self):
        """method to fetch allusers registered"""
        users = UserModels.fetch_all(self)
        if not users:
            return {"message": "No user found"}, 404
        return {"status": "Ok",
                "results": len(UserModels.users),
                "users": users}, 200


class User(Resource):
    """class to handle single user access, updates and deleting"""
    def get(self, user_id):
        user = UserModels.fetch_user_by_userid(user_id)
        if not user:
            return { "message": "user not found"}, 404
        return user

    def delete(self, user_id):
        user = UserModels.fetch_user_by_userid(user_id)
        if not user:
            return {
                "message": "That user does not exist"
            }, 404
        UserModels.delete_user(user)
        return {
                   "message": "User has been deleted",
                   "users": len(UserModels.users)
               }, 201


class LoginManager(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument('email', type=str, required=True, help="Please input an email")
        self.parser.add_argument('password', type=str, required=True, help="Please enter a password")

    # login should not use get because get exposes the user's inputs in the url bar
    def post(self):
        """register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        email = args['email']
        password = args['password']

        user = UserModels.fetch_user_by_email(email)
        if not user or password != user['password']:
            return { "message": "Wrong login credentials"}, 400
        return {"message": "Login successful"}, 200


