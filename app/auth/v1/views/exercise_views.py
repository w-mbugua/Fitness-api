import json

from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.exercise import ExerciseModel
from flask_restful.reqparse import RequestParser
from ..model.exercise import ExerciseModel
from app.utilities.validator import Validators

validate = Validators() # an instance of the validators class

class Exercise(Resource):
    """class to handle exercise endpoints"""
    def __init__(self):
        # when you enter the wrong things itn the url for instance, you get this helper messages
        self.parser = RequestParser()
        self.parser.add_argument("name", type=str, required=True, help="Name of the exercise is required")
        self.parser.add_argument("period", type=int, required=True, help="Please input how log the exercise should take")
        self.parser.add_argument("description", type=str, required=True, help="Please provide a description for the exercise")

    #GET read,
    def get(self):
        """get all exercises"""
        exercises = ExerciseModel.get_all_exercises(self)
        return {
            "exercises": exercises

        }

    #POST, create
    def post(self):
        """post new exercises"""
        args = self.parser.parse_args()
        args = request.get_json()
        name = args['name']
        period = args['period']
        description = args['description']

        if validate.exercise_exists(name, description):
            return {
                "status": 400,
                "error": "exercise already exists"
            }
        new_exercise = ExerciseModel(name, period, description)
        new_exercise.save()
        return {
                "status": 201,
                "message": "exercise successfully created",
                "exercise": new_exercise.__dict__
            }

        #upadte

        # delete

