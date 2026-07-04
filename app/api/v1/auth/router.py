from typing import Any

from flask import Blueprint, request
from pydantic import ValidationError

from schemas import LoginRequest

from app.api.v1.auth.schemas import LoginResponse

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.post("/login")
def login()-> LoginResponse | Any:
    # JWT 의존성 부여 해야 함
    try:
        data:dict = request.get_json()
        login_request = LoginRequest(**data)

    except ValidationError as e:
        raise e
    return LoginResponse