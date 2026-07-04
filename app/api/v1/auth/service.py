class AuthService:
    def __init__(self, UserRepo):
        self.user_repo = UserRepo

    def login(self, user_data):
        email = user_data.email
        password = user_data.password
        try:
            user_token = self.user_repo.loginCheck(email = email, password = password)
        except Exception as e:
            raise e
        return user_token
