# Third party libreries
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData

# Owns libraries
from app.config.config import settings

class Database:

    def __init__(self, _test=False) -> None:
        self.url = self._create_url(
            _engine      = settings.engine,
            _db_user     = settings.db_user,
            _db_password = settings.db_password,
            _db_host     = settings.db_host,
            _db_port     = settings.db_port,
            _database    = settings.database
        )
        self.test = _test
        self.engine = create_engine(self.url)
        self.meta = MetaData()

    def _create_url(self, _engine, _db_user, _db_password, _db_host, _db_port, _database):
        return f'{_engine}://{_db_user}:{_db_password}@{_db_host}:{_db_port}/{_database}'

db = Database()