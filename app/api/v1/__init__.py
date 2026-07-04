from flask import Blueprint

from app.api.v1.endpoints import conflicts

# v1 하위 엔드포인트들을 모으는 상위 Blueprint.
# FastAPI에서 api_router.include_router(...) 하는 것과 같은 역할.
api_v1 = Blueprint("api_v1", __name__)

api_v1.register_blueprint(conflicts.bp)
