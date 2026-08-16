from typing import Callable
import time
from fastapi import FastAPI, status, Depends, APIRouter, HTTPException, Header
from fastapi.security import HTTPBearer

from app.api.dependencies import get_user_service
from app.schemas.user_schemas import (RegisterUser, ResponseUser, LoginUser, LoginUserResponse, Refresh, RefreshResponse,
                                      LogoutUser)
from app.services.user import UserService
from app.schemas.errors import *
router = APIRouter(prefix='/api/v1/auth')
security = HTTPBearer()


# def runtime_deco(func: Callable):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(time.time() - start)
#         return result
#
#     return wrapper


# @runtime_deco
@router.post("/register", status_code=status.HTTP_201_CREATED)
def user_register(payload: RegisterUser,
                  user_service: UserService =  Depends(get_user_service)):

    try:
        return user_service.create_user(payload)
    except Exception as  e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login", status_code=status.HTTP_200_OK)
def user_login(payload: LoginUser,
               user_service: UserService =  Depends(get_user_service)):
    try:
        return user_service.login_user(payload)
    except Exception as  e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))



@router.post("/refresh", status_code=status.HTTP_200_OK)
def user_refresh(payload: Refresh,
                 user_service: UserService =  Depends(get_user_service)):
    try:
        return user_service.refresh_access_token(payload)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def user_logout(payload: LogoutUser, authorization = Depends(security),
                user_service: UserService =  Depends(get_user_service)):
    try:
        return user_service.logout_user(authorization, payload)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# @router.get("/test")
# def test(authorization: str = Header()):
#     return {"authorization": authorization}