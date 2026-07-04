from sqlalchemy.orm import Session

from .security import JwtService
from ..api.v1.auth.service import AuthService
from ..api.v1.auth.repo import UserRepository
# 추후 완전한 DI 패턴 교체 희망 -> 지금 형태는 이름만 컨테이너이고 실제는 X
class Container:
    def __init__(self, db:Session):
        self.db = db

    def get_user_repository(self) -> UserRepository: return UserRepository(db = self.db, jwt_service=self.get_jwt_service())
    def get_auth_service(self) -> AuthService: return AuthService(user_repo=self.get_user_repository())
    def get_jwt_service(self) -> JwtService: return JwtService(secret_key = "3")