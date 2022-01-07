from typing import Dict, List, Optional
from pydantic.class_validators import validator
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import StrictStr
from datetime import date


class CreateUserSchema(BaseModel):
    nombre_usuario:             StrictStr
    email_usuario:              EmailStr
    telefono_usuario:           str
    password_usuario:           str
    repeat_password_usuario:    str
    activo_usuario:             Optional[bool]= True


    class Config:
        title= "CreateUserSchema"
        validate_all = True

    @validator('repeat_password_usuario')
    def passwords_match(cls, v, values, **kwargs):
        if 'password_usuario' in values and v != values['password_usuario']:
            raise ValueError('passwords do not match')
        return v

class CreateUserSuccessSchema(BaseModel):
    status: bool = True
    message: str = "Usuario registrado exitosamente"
    id_usuario: int
    