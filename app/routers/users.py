# Third party libreries
from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Path
from fastapi.responses import JSONResponse

# Owns libraries
from app.schemas.user import CreateUserSchema, CreateUserSuccessSchema, GetOneUserSuccessSchema, GetAllUsersSuccessSchema
from app.controllers.user import UserController

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.get("/")
def get_all_users():
    """
    Enpoint que regresa todos los usuarios. Este servicio regresa usuarios activos e inactivos, y no requiere parametros.
    """
    try:
        user_controller = UserController()
        all_users = user_controller.get()
        # print(f"numero de usuarios -> {len(all_users)}")

        return GetAllUsersSuccessSchema( data=all_users )
    except Exception as error:
        print( { "Error": "GET", "name": "get_users", "detail": error.statement, "code": error.code } )
        raise ValueError({ "Error": "GET", "nameFunction": "get_users", "detail": error})


@router.get("/{id}/")
def get_one_user(id: int = Path(...)):
    """
    Método que se va a traer un usuario
    Request: El ID del usuario
    Response: se va traer toda la información del usuario
    """
    try:
        user_controller = UserController()
        one_user = user_controller.get(id)
        # print(one_user)
        if one_user is None:
            return JSONResponse(status_code=400, content={"status": False, "detail": [{"msg": "user not found", "loc": ["path", "id"]}], "data": [] })
        
        return GetOneUserSuccessSchema( data=one_user )
    except Exception as error:
        print( { "Error": "Exception", "nameFunction": "get_one_user", "detail": error } )
        raise ValueError({ "Error": "Exception", "nameFunction": "get_one_user", "detail": error})


@router.post("/crear/")
def create_user(user: CreateUserSchema):
    """
    Crea usuario apartir del modelo dado. 

        Response: Va a crear un contacto
                200: message: "Usuario registrado exitosamente", usuario_id: 10, status: true
                400: Usuario ya registrado.
                502: Hubo un problema al crear el usuario
    """
    try:
        
        user_controller = UserController()
        id_new_user = user_controller.create_user(user)

        if id_new_user is False:
                return JSONResponse(status_code=400, content={"status": False, "detail": [{"msg": "User already exists", "loc": ["body", "repeated_email", "or", "repeated_tel"]}], "data": [] })
    
        
        return CreateUserSuccessSchema( id_usuario=id_new_user )
    except Exception as error:
        print( { "Error": "Exception", "nameFunction": "create_user", "detail": error } )
        raise ValueError({ "Error": "Exception", "nameFunction": "create_user", "detail": error})
