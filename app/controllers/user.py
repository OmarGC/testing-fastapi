#Third party libraries
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import or_, select

# Owns libraries
from app.controllers.base_controller import BaseController
from app.models.user import user
from app.schemas.user import CreateUserSchema
from app.utils.cryptography.password import encrypt_password, check_password

class UserController(BaseController):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = user

    
    def get_user_email(self, email: str):
        try:
            conn = self.database.engine.connect()
            result = conn.execute(
                self.model.select().where( self.model.c.email_usuario == email )
            ).first()
            conn.close()
            return result
        except SQLAlchemyError as error:
            print( { "Error": "SQLAlchemyError", "nameFunction": "get_user_email", "detail": error } )

    def create_user(self, user: CreateUserSchema):
        try:
            # Busca si existe usuario por email
            conn = self.database.engine.connect()

            stmt_select = self.model.select().where(
                or_(
                    self.model.c.email_usuario == user.email_usuario,
                    self.model.c.telefono_usuario == user.telefono_usuario
                )
            )
           
            find_user = conn.execute( stmt_select ).first()
            
            if find_user:
                return False
            
            new_user = user.copy(
                exclude={ 'repeat_password_usuario' },
                update={ 'password_usuario': encrypt_password(user.password_usuario) }
            )


            return super().create(new_user.dict())

        except SQLAlchemyError as error:
            print( {
                "Error": type(error).__name__,
                "nameFunction": "create",
                "detail": error,
                "type": type(error)
            } )
    