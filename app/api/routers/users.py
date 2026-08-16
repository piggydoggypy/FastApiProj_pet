
from fastapi import FastAPI, status, Depends, APIRouter
from fastapi.security import HTTPBearer

from app.api.dependencies import get_user_service
from app.schemas.user_schemas import (RegisterUser, ResponseUser, LoginUser, LoginUserResponse, Refresh,
                                      RefreshResponse,
                                      LogoutUser, ChangeUsername, ChangePassword)
from app.services.user import UserService
from app.services.token_funcs import verify_token

router = APIRouter(prefix='/api/v1/users')
security = HTTPBearer()


@router.post("/me", status_code=status.HTTP_200_OK)
def user_register(authorization = Depends(security),
        user_service: UserService =  Depends(get_user_service)):
    return user_service.get_me(authorization)

@router.patch("/me", status_code=status.HTTP_200_OK)
def user_register(payload: ChangeUsername,
                  authorization = Depends(security),
                  user_service: UserService =  Depends(get_user_service)):
    return user_service.change_username(authorization, payload)

@router.patch("/password", status_code=status.HTTP_200_OK)
def user_register(payload: ChangePassword,
                  authorization = Depends(security),
                  user_service: UserService =  Depends(get_user_service)):
    return user_service.change_password(authorization, payload)
