from flask import jsonify, make_response, request
from flask_restful import Resource
from ..model.exercise import ExerciseModel
from flask_restful.reqparse import RequestParser
from ..model.workout_routine import WorkoutRoutineModel

class WorkoutRoutine(Resource):
    """
    Class for handling workout routine endpoints.
    """

    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument("workout", type=str, required=True, help="The type of workout is required. For example, push-ups.")
        self.parser.add_argument("sets", type=int, required=True, help="Please enter the number of sets.")
        self.parser.add_argument("duration_in_mins", type=int, required=True, help="Please enter the duration of the workout which should be in minutes.")
        self.parser.add_argument("complete", type=bool, required=True, help="Please enter a boolean response, True for complete, False for NOT complete.")

    def post(self):
        """
        Craete new workout routines.
        """

        args = self.parser.parse_args()
        args = request.get_json()
        workout = args['workout']
        sets = args['sets']
        duration_in_mins = args['duration_in_mins']
        complete = args['complete']

        new_workout_routine = WorkoutRoutineModel(workout, sets, duration_in_mins, complete)

        return {
            "message": "The workout routine has been created!",
            "workout_routine": new_workout_routine.__dict__
        }