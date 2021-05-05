from flask import Blueprint
from flask_restful import Api
from .views.user_views import Users
from .views.exercise_views import Exercise
from .views.workout_routine_views import WorkoutRoutine
version1 = Blueprint('auth_v1', __name__)

api = Api(version1, catch_all_404s=True)

api.add_resource(Users, '/auth/register', strict_slashes=False) #change to /auth/register

api.add_resource(Exercise, '/exercises/', strict_slashes=False)

api.add_resource(WorkoutRoutine, '/workout-routines/', strict_slashes=False)