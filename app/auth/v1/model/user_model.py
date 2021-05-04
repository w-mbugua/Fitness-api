"""User Model"""

class UserModels:
    """ class for user operations"""

    users = []

    def __init__(self, email, password, confirm_password):
        """Init a User Model"""

        self.userId = len(UserModels.user) + 1 
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def register(self):
        """ Method to SignUp a User """
        data = dict(
            userID= self.userId,
            email = self.email,
            password = self.password,
            confirm_password = self.confirm_password
        )
        self.user.append(data)
        return self.users

    def fetch_user_by_userId(self, userId):
        """ Get an instance of a user using their Id """
        for user in users:
            if user["userId"] == userId:
                return user