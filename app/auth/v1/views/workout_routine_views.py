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
        self.parser.add_argument("username", type=str, required=True, help="Please your preferred username.")

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
        username = args['username']

        new_workout_routine = WorkoutRoutineModel(workout, sets, duration_in_mins, complete, username)
        new_workout_routine.save_workout_routine()

        return {
            "status": 201,
            "message": "The workout routine has been created!",
            "workout_routine": new_workout_routine.__dict__
        }

    def get(self):
        """
        Method for getting a workout routine by id.
        """

        workout_routines = WorkoutRoutineModel.get_all_workout_routines(self)

        return {
            "status": 200,
            "Workout routine": workout_routines
        }

    def put(self):
        """
        Mehtod for updating workout routine.
        """

        workout_complete = WorkoutRoutineModel.workout_complete(self)

        return {
            "message": "The workout routine have been completed!"
        }

    def delete(self):
        """
        Method for deleting workout routine.
        """

        workout_delete = WorkoutRoutineModel.workout_delete(self)

        return {
            "message": "The workout routine has been deleted."
        }