from typing import Any

from flask import Blueprint, request
from pydantic import ValidationError

from schemas import LoginRequest, LoginResponse
from ....core.wrapper_container_for_call import get_auth_service

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.post("/login")
def login()-> LoginResponse | Any:
    # JWT 의존성 부여 해야 함
    try:
        data:dict = request.get_json()
        login_request = LoginRequest(**data)
        auth_service = get_auth_service()
        auth_service.login(user_data = login_request)
        token = auth_service
    except ValidationError as e:
        raise e
    return LoginResponse()