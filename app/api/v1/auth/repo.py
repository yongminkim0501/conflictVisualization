from app.core.security import generate_jwt
from app.core.error_handler import NotMatchPassword

class UserRepository:
    def __init__(self, db):
        self.db = db

    def check_login(self, email, password)->str:
        user = self.db.find_user_by_email(email)
        if self.db.check_password(user, password):
            generated_jwt:str = generate_jwt(user)
        else:
            raise NotMatchPassword

        return generated_jwt