from flask import Blueprint
from flask_restful import Api
from .views.user_views import Users, User, RegistrationManager, LoginManager
from .views.exercise_views import Exercise, SingleExercise
from .views.workout_routine_views import WorkoutRoutine, SingleRoutine
version1 = Blueprint('auth_v1', __name__)

api = Api(version1, catch_all_404s=True)

api.add_resource(Users, '/users')
api.add_resource(RegistrationManager, '/users/register')
api.add_resource(LoginManager, '/users/login')
api.add_resource(User, '/users/<int:user_id>')

api.add_resource(Exercise, '/exercises')
api.add_resource(SingleExercise, '/exercises/<int:id>')

api.add_resource(WorkoutRoutine, '/workout-routines/')
api.add_resource(SingleRoutine, '/workout-routines/<int:id>')

