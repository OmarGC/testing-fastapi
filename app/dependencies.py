# Third party libreries
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette import status

# Owns libraries
from app.config.config import settings


def get_api_key(api_key_header: str = Security( APIKeyHeader(name="x-api-key", auto_error=True) )):
    if api_key_header != settings.x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )