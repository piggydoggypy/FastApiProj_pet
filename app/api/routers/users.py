from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from app.api.dependencies import get_user_service
from app.schemas.user_schemas import (
    ChangePassword,
    ChangeUsername,
)
from app.services.user import UserService

router = APIRouter(prefix="/api/v1/users")
security = HTTPBearer()


@router.post("/me", status_code=status.HTTP_200_OK)
def user_post(
    authorization=Depends(security),
    user_service: UserService = Depends(get_user_service),
):
    return user_service.get_me(authorization)


@router.patch("/me", status_code=status.HTTP_200_OK)
def user_patch(
    payload: ChangeUsername,
    authorization=Depends(security),
    user_service: UserService = Depends(get_user_service),
):
    return user_service.change_username(authorization, payload)


@router.patch("/password", status_code=status.HTTP_200_OK)
def user_password(
    payload: ChangePassword,
    authorization=Depends(security),
    user_service: UserService = Depends(get_user_service),
):
    return user_service.change_password(authorization, payload)
