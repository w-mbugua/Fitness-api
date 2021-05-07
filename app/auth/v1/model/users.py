"""users model"""

class UserModels:
    """class for user operations"""

    users = []

    def __init__(self, first_name, last_name, age, email, password, confirm_password):
        """init a user model"""
        self.userId = len(UserModels.users) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def register(self):
        """method to signup a user"""
        data = dict(
            userId=self.userId,
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.age,
            email=self.email,
            password=self.password,
            confirm_password=self.confirm_password
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
    @classmethod
    def fetch_user_by_email(cls, email):
        """access a user using their id"""
        for user in UserModels.users:
            if user['email'] == email:
                return user
    # reading all the users
    def fetch_all(self):
        """get all data"""
        return UserModels.users

    def delete_user(self):
        return UserModels.users.remove(self)






