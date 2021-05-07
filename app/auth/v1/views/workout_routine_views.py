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
        self.parser.add_argument("workout", type=str, required=True, help="The type of workout is required. For example, upperbody workout.")
        self.parser.add_argument("sets", type=list, required=True, help="Please enter the number of sets.")
        self.parser.add_argument("duration_in_mins", type=int, required=True, help="Please enter the duration of the workout which should be in minutes.")
        self.parser.add_argument("complete", type=bool, required=True, help="Please enter a boolean response, True for complete, False for NOT complete.")
        # self.parser.add_argument("username", type=str, required=True, help="Please enter your preferred username.")

    def get(self):
        routines = WorkoutRoutineModel.get_workout_plans(self)
        if not routines:
            return {
                "status": 404,
                "message": "No routines found"
            },404
        else:
            return {
                "status": "Ok",
                "work_out_routines": routines
            },200

    def post(self):
        """
        Create new workout routines.
        """
        args = self.parser.parse_args()
        args = request.get_json()
        workout = args['workout']
        sets = args['sets']
        duration_in_mins = args['duration_in_mins']
        complete = args['complete']
        # username = args['username']

        new_workout_routine = WorkoutRoutineModel(workout, sets, duration_in_mins, complete)

        new_workout_routine.save_workout_routine()

        return {
            "status": 201,
            "message": "The workout routine has been created!",
            "workout_routine": new_workout_routine.__dict__
        }


class SingleRoutine(Resource):
    """class to manage one routine"""
    def get(self, id):
        routine = WorkoutRoutineModel.get_workout_routine_by_id(id)
        if not routine:
            return {
                   "status": 404,
                   "message": "No routines found"
               }, 404
        else:
            return {
               "status": "Ok",
               "work_out_routine": routine
           }, 200

    def put(self, id):
        """
        Method for updating workout routine.
        """
        routine = WorkoutRoutineModel.get_workout_routine_by_id(id)
        if not routine:
           return { "message": "That workout does not exist" }, 400
        else:
            routine['complete'] = True
            return {"message": "The workout has been completed!"}


    def delete(self, id):
        """method to delete a single workout routine"""
        routine = WorkoutRoutineModel.get_workout_routine_by_id(id)
        if not routine:
            return {"message": "That routine does not exist"}, 404
        WorkoutRoutineModel.delete_workout(routine)
        return {"message": "routine item successfully deleted"}, 200


