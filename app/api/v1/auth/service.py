class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def login(self, user_data):
        email = user_data.email
        password = user_data.password
        try:
            user_token = self.user_repo.loginCheck(email = email, password = password)
        except Exception as e:
            raise e
        return user_token
