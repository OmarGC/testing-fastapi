from logging import error
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import select
from sqlalchemy.sql import text
# Owns libraries
from app.config.connection import Database


class BaseController():

    def __init__(self) -> None:
        self.model = None
        self.database = Database()

    def get(self, id: Optional[int] = None):
        """ Método para obtener todos los registros, si el parametro id existe obtiene 1 registro. """
        try:
            conn = self.database.engine.connect()
            if id:
                one = conn.execute(
                    self.model.select().where( text(f"id_{str(self.model).lower()}= {id}")  )
                ).first()
                return one
            
            all = conn.execute(
                self.model.select()
            ).fetchall()
            return all
        except Exception as error:
            print({
                "Error": type(error).__name__,
                "nameFunction": "get_all",
                "detail": error,
                "type": type(error)
            })


    def create(self, *args, **kwargs) -> int:
        """ Método para crear un registro en la db, retorna el id. """
        try:
            conn = self.database.engine.connect()
            result = conn.execute(
                self.model.insert().values(*args, **kwargs)
            )
            conn.close()
    
            return result.lastrowid
        except Exception as error:
            print( {
                "Error": type(error).__name__,
                "nameFunction": "base_create",
                "detail": error,
                "type": type(error)
            } )
