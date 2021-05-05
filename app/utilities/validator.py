"""validation"""
import re
from ..auth.v1.model.users import UserModels
from ..auth.v1.model.exercise import ExerciseModel
class Validators:
    """class to hold validation methods"""

    def valid_email(self, email):
        """method to validate emails"""
        # uses regular expressions
        reg_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return re.match(reg_email, email)

    def user_exists(self, email):
        """check if a user exists"""
        user = UserModels.fetch_user_by_email(self, email)
        if user:
            return {
                "status": 400,
                "error": "That email already exists"
            }

    # validates against repetition of the same exact workout types
    def exercise_exists(self, name, period):
        """check if an exercise type already exists"""
        exercises = ExerciseModel.get_all_exercises(self)
        for exercise in exercises:
            if exercise['name'] == self.name and exercise['period'] == self.period:
                return {
                    "status": 400,
                    "error": "That workout type already exists"
                }


