from flask import Blueprint
from flask_restful import Api
from .views.user_views import Users, User
from .views.exercise_views import Exercise, SingleExercise
from .views.workout_routine_views import WorkoutRoutine
version1 = Blueprint('auth_v1', __name__)

api = Api(version1, catch_all_404s=True)

api.add_resource(Users, '/users', strict_slashes=False)
api.add_resource(User, '/users/<int:user_id>', strict_slashes=False)
api.add_resource(Exercise, '/exercises', strict_slashes=False)
api.add_resource(SingleExercise, '/exercises/<int:id>', strict_slashes=False)
# api.add_resource(Exercise, '/workout-routines/id', strict_slashes=False)

api.add_resource(WorkoutRoutine, '/workout-routines/', strict_slashes=False)