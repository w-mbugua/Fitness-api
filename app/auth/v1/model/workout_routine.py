""" Workout Routine model """
from .users import UserModels

class WorkoutRoutineModel:

    workout_routines = []

    def __init__(self, workout, sets, duration_in_mins, complete, username):
        self.id = len(WorkoutRoutineModel.workout_routines) + 1
        self.workout = workout
        self.sets = sets
        self.duration_in_mins = duration_in_mins
        self.complete = complete
        self.username = username

    def save_workout_routine(self):
        data = dict(
            id = self.id,
            workout = self.workout,
            sets = self.sets,
            duration_in_mins = self.duration_in_mins,
            complete = self.complete,
            username = self.username
        )
        WorkoutRoutineModel.workout_routines.append(data)

    def get_workout_routine_by_id(self, id):
        for workout_routine in WorkoutRoutineModel.workout_routines:
            if workout_routine['id'] == self.id:
                return workout_routine

    def get_all_workout_routines(self):
        return WorkoutRoutineModel.workout_routines

    def workout_complete(self):
        for workout_routine in WorkoutRoutineModel.workout_routines:
            workout_routine['complete'] = True
        return WorkoutRoutineModel.workout_routines