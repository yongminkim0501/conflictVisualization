from flask import g

from app.core.container import Container
from app.api.v1.auth.service import AuthService

def get_container() -> Container:
    return g.container

def get_auth_service() -> AuthService:
    return get_container().get_auth_service()
