from __future__ import annotations

from flask import Flask, jsonify
from flask_cors import CORS

from app.api.v1 import api_v1


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)

    if config:
        app.config.update(config)

    # 프론트(Next.js dev, Streamlit 등)가 다른 origin에서 호출하므로 CORS 허용.
    # 배포 시엔 origins를 실제 프론트 도메인으로 좁히는 걸 권장.
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # 버전별 API blueprint 등록 (FastAPI의 include_router에 해당)
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app
