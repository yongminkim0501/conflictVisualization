from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ENV: str = "local"
    CORS_ORIGINS: str = "*"

    # MariaDB
    MARIADB_HOST: str
    MARIADB_PORT: str
    MARIADB_USERNAME: str
    MARIADB_PASSWORD: str
    MARIADB_DATABASE: str

    @property
    def MARIADB_URL(self) -> str:
        return (f'mariadb+pymysql://{self.MARIADB_USERNAME}:{self.MARIADB_PASSWORD}'
                f'@{self.MARIADB_HOST}:{self.MARIADB_PORT}'
                f'/{self.MARIADB_DATABASE}?charset=utf8mb4')

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int
    REDIS_SSL: bool

    @property
    def REDIS_URL(self) -> str:
        protocol = "rediss" if self.REDIS_SSL else "redis"

        if self.REDIS_PASSWORD:
            return f"{protocol}://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        else:
            return f"{protocol}://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    ALGORITHM : str
    SECRET_KEY : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_MINUTES : int

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
