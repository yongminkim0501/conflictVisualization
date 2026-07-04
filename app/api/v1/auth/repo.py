class UserRepository:
    def __init__(self, db, jwt_service):
        self.db = db
        self.jwt_service = jwt_service

    def check_login(self, email, password)->str:
        user = self.db.find_user_by_email(email)
        if self.db.check_password(user, password):
            generated_jwt:str = self.jwt_service.create_jwt(user)
        else:
            raise "NotMatchPassword"

        return generated_jwt