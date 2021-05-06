""" workout routine model """

class RoutineModels:

    routines = []

    def __init__(self,routine_name,workout_type,number):
        """init routine model"""
        self.routineId = len(RoutineModels.Routine)+1
        self.routine_name = routine_name
        self.workout_type =  workout_type
        self. number = number   #the number of workout_types     

    def register(self):
        """ method to register routine """ 
        data = dict(
            routineId = self.routineId,
            routine_name = self.routine_name,
            workout_type = self.workout_type,
            number = self.number 
        )
        self.Routine.append(data)
        return self.Routine

    def fetch_routine_by_routineId(self,routineId):
        """get an instance of routine using their id"""
        for routine in routines:
            if routine["routineId"] == routineId:
                return routine
