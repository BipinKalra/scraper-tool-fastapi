from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from services.authentication import AuthenticationService


def authenticate(authorization: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]):
    token_type, token = authorization.credentials.split()

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        return AuthenticationService().authenticate(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
