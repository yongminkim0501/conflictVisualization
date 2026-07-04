from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, database_url : str = ""):
        self.engine = create_engine(
            database_url,
            echo = True,
            pool_pre_ping=True,
        )
        self.SessionLocal = sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False
        )

    def get_local_session(self):
        return self.SessionLocal()