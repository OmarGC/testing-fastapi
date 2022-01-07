from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import date, datetime
from pydantic.types import StrictStr
from pydantic.networks import EmailStr


class UserSchema(BaseModel):
    id_usuario:                 Optional[int]
    created_at:                 Optional[date]
    updated_at:                 Optional[date]
    nombre_usuario:             StrictStr
    apellido_paterno_usuario:   Optional[StrictStr]
    apellido_materno_usuario:   Optional[StrictStr]
    email_usuario:              EmailStr
    telefono_usuario:           str
    activo_usuario:             bool



class GetOneUserSuccessSchema(BaseModel):
    status: bool = True
    data: UserSchema


class GetAllUsersSuccessSchema(BaseModel):
    status: bool = True
    data: List[UserSchema]
