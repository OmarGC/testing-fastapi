#Third party libraries
from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.sqltypes import Boolean, Integer, String, DateTime, Date
from sqlalchemy.sql.functions import func

#Own's Libraries
from app.config.connection import db

user = Table(
    "USUARIO",
    db.meta,
    Column( "id_usuario", Integer, primary_key=True, nullable=False ),
    Column( "created_at", DateTime(timezone=True), server_default=func.now(), nullable=False ),
    Column( "updated_at", DateTime(timezone=True), onupdate=func.now(), nullable=True ),
    Column( "nombre_usuario", String(120), nullable=False ),
    Column( "apellido_paterno_usuario", String(120), nullable=True ),
    Column( "apellido_materno_usuario", String(120), nullable=True ),
    Column( "email_usuario", String(150), nullable=False, unique=True ),
    Column( "telefono_usuario", String(20), nullable=False, unique=True ),
    Column( "activo_usuario", Boolean, nullable=False )
)

db.meta.create_all(db.engine)