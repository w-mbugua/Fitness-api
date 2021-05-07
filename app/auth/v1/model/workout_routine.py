""" Workout Routine model """
from .users import UserModels

class WorkoutRoutineModel:

    workout_routines = []

    def __init__(self, workout, sets, duration_in_mins, complete):
        self.id = len(WorkoutRoutineModel.workout_routines) + 1
        self.workout = workout
        self.sets = sets
        self.duration_in_mins = duration_in_mins
        self.complete = complete
        # self.username = username


    def save_workout_routine(self):
        data = dict(
            id = self.id,
            workout = self.workout,
            sets = self.sets,
            duration_in_mins = self.duration_in_mins,
            complete = self.complete,
            # username = self.username
            )
        WorkoutRoutineModel.workout_routines.append(data)
        return self.workout_routines

    @classmethod
    def get_workout_routine_by_id(cls, id):
        for workout_routine in WorkoutRoutineModel.workout_routines:
            if workout_routine['id'] == id:
                return workout_routine


    def workout_complete(self, id):
        workout = WorkoutRoutineModel.get_workout_routine_by_id(id)
        workout['complete'] = True
        return workout


    def workout_delete(self):
        return WorkoutRoutineModel.workout_routines.clear()

    def delete_workout(self):
        return WorkoutRoutineModel.workout_routines.remove(self)

    # def get_all_workout_routines(self, user_id):
    #     user_workout_routine = []
    #
    #     for workout_routine in WorkoutRoutineModel.workout_routines:
    #         if workout_routine['user_id'] == self.user_id:
    #             user_workout_routine.append(workout_routine)
    #     return user_workout_routine

    def get_workout_plans(self):
        return WorkoutRoutineModel.workout_routines

