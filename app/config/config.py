# Third party libreries
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    app_name: str = 'testing-fastapi'
    version: str = '0.1.0'
    environment: str
    x_api_key: str
    database: str
    db_host: str
    db_user: str
    db_password: str
    db_port: int = 3306
    engine: str = 'mysql+pymysql'
    jwt_secret: str
    jwt_algorithm: str = 'HS256'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()