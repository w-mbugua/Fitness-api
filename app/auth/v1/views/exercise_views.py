import json

from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.exercise import ExerciseModel
from flask_restful.reqparse import RequestParser
from ..model.exercise import ExerciseModel
from app.utilities.validator import Validators

validate = Validators() # an instance of the validators class

class SingleExercise(Resource):
    def get(self, id):
        exercise = ExerciseModel.get_exercise_by_id(id)
        if exercise:
            return{
                "status": 200,
                "exercise": exercise
            }, 200
        else:
            return {
                "status": 404,
                "message": "No exercise found"
            }, 404

    def delete(self, id):
        exercise = ExerciseModel.get_exercise_by_id(id)
        if not exercise:
            return {"message": "That exercise does not exist"}, 404
        ExerciseModel.delete_ex(exercise)
        return {"message": "Exercise item successfully deleted"}, 200


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
        exercises = ExerciseModel.get_all_exercises()
        if not exercises:
            return {"message": "No exercises found"}, 404
        return {
            "status": "ok",
            "results": len(ExerciseModel.exercises),
            "exercises": exercises}

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
                "message": "exercise successfully created",
                "exercise": new_exercise.__dict__
            }, 201

