from flask import Flask, g

from app.database.database_session import Database

from app.core.container import Container

def create_app():
    app = Flask(__name__)

    @app.before_request
    def open_container():
        db = Database.get_local_session()
        g.container = Container

    @app.teardown_request
    def close_container(error=None):
        container = getattr(g, "container", None)
        if container is None:
            return
        if error:
            container.db.rollback()
        else:
            container.db.commit()
        container.db.close()
    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
