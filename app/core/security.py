from datetime import datetime, timedelta, timezone

from app.models.user_model import User

class JwtService:
    def __init__(
            self,
            secret_key : str,
            algorithm: str="HS256",
            expire_minutes:int=60
    ):
        self.secret_key = secret_key

    def generate_jwt(user: User):
        now = datetime.now(timezone.utc)
