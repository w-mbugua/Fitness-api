"""users model"""

class UserModels:
    """class for user operations"""

    users = []

    def __init__(self, email, password, confirm_password):
        """init a user model"""
        self.userId = len(UserModels.users) + 1
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def register(self):
        """method to signup a user"""
        data = dict(
        userId =self.userId,
        email = self.email,
        password = self.password,
        confirm_password = self.confirm_password
        )
        self.users.append(data)
        return self.users

    @classmethod
    def fetch_user_by_userid(cls, user_id):
        """access a user using their id"""
        for user in UserModels.users:
            if user['userId'] == user_id:
                return user

    # fetch user by email
    def fetch_user_by_email(self, email):
        """access a user using their id"""
        for user in UserModels.users:
            if user['email'] == email:
                return user
    # reading all the users
    def fetch_all(self):
        """get all data"""
        return UserModels.users




