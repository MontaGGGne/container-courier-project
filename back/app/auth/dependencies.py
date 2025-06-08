from datetime import datetime

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from app.auth.dao import AuthDAO
from app.auth.schemas import CLogin
from app.config import settings


def get_token(request: Request):
    token = request.headers.get("Authorization")

    if not token:
        token = request.cookies.get("access_token")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing authorization token",
            )
    return token


async def get_current_user(token: None | str = Depends(get_token)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, "HS256")
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from e
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    email: str = payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await AuthDAO.find_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


async def get_current_staff(current_user: CLogin = Depends(get_current_user)):
    if not current_user.staff:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return current_user
