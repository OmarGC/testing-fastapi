# Third party libreries
from fastapi import FastAPI, Depends, Request 
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

# Owns libraries
from app.config.config import settings
from app.dependencies import get_api_key
from app.routers import users


# Description text
DESC_TEXT = "Api rest creada por Omar gc con el fin de testear vulnerabilidades dentro de la imagen docker y de las librerias usadas por fastapi. Para el uso de nuestra `API-REST`, es necesario contar con `ApiKey` válida."

app = FastAPI(
    title=settings.app_name,
    description=DESC_TEXT,
    version=settings.version,
    dependencies=[Depends(get_api_key)]
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "status": False,
            "detail": exc.errors(),
            "data": [],
            # "body": exc.body
        }),
    )

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    """
    Metodo root el cual no recibe ningun parametro, su funcion es ver el entorno de la api.
    """
    return { "message": "welcome to the API", "environment": settings.environment }

# Routes api
app.include_router(users.router)
