from datetime import datetime

from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.models.users import UsersORM
from app.repository.user import UserRepository
from app.schemas.errors import WrongEmail, WrongPassword
from app.schemas.user_schemas import (
    ChangePassword,
    ChangeUsername,
    LoginUser,
    LoginUserResponse,
    Refresh,
    RefreshResponse,
    RegisterUser,
    ResponseUser,
)
from app.services.token_funcs import (
    create_access_token,
    create_refresh_token,
    verify_token,
)
from app.services.validate_funcs import (
    validate_email,
    validate_password,
    validate_username,
)


class UserService:
    def __init__(
        self,
        db: Session,
    ) -> None:
        self.db = db
        self.user_repository = UserRepository(db)

    """Работает, сделано на 100%"""



    def create_user(self, payload: RegisterUser) -> ResponseUser:
        try:
            usernames = self.user_repository.get_all_usernames()
            validate_username(payload.username, usernames)
            emails = self.user_repository.get_all_emails()
            validate_email(payload.email, emails)
            validate_password(payload.password)
        except Exception as e:
            raise e

        new_user = UsersORM(
            username=payload.username,
            email=payload.email,
            password=payload.password,
            role="EMPLOYEE",
            created_at=str(datetime.now().date()),
        )
        self.user_repository.create_user(new_user)
        created_user = self.user_repository.get_by_email(payload.email)
        self.db.commit()

        return ResponseUser(
            id=created_user.id,
            username=new_user.username,
            email=new_user.email,
            role=new_user.role,
        )

    def login_user(self, payload: LoginUser) -> LoginUserResponse:
        user = self.user_repository.get_by_email(payload.email)
        if user is None:
            raise WrongEmail("Неправильный email")

        if user.password != payload.password:
            raise WrongPassword("Неправильный пароль")

        return LoginUserResponse(
            access_token=create_access_token(user.id),
            refresh_token=create_refresh_token(user.id),
            token_type="Bearer",
        )

    def refresh_access_token(self, payload: Refresh) -> RefreshResponse:
        try:
            user_id = verify_token(payload.refresh_token).get("sub")

            response = RefreshResponse(
                access_token=create_access_token(user_id), token_type="Bearer"
            )
            return response
        except Exception as e:
            raise e

    def logout_user(self, authorization, payload) -> None:
        try:
            verify_token(authorization.credentials)
            verify_token(payload.refresh_token)
        except Exception as e:
            raise e

    def get_me(self, authorization: HTTPAuthorizationCredentials):
        credentials = authorization.credentials
        try:
            info = verify_token(credentials)
            return self.user_repository.get_by_id(info["sub"])
        except Exception as e:
            raise e

    def change_username(
        self, authorization: HTTPAuthorizationCredentials, payload: ChangeUsername
    ):
        credentials = authorization.credentials
        try:
            info = verify_token(credentials)
            self.user_repository.change_username(info["sub"], payload.username)
            self.db.commit()
        except Exception as e:
            raise e

    def change_password(
        self, authorization: HTTPAuthorizationCredentials, payload: ChangePassword
    ):
        credentials = authorization.credentials
        try:
            info = verify_token(credentials)
            if (
                payload.current_password
                == self.user_repository.get_by_id(info["sub"]).password
            ):  # потом сделать проверку на хеш
                self.user_repository.change_password(
                    info["sub"], payload.new_password
                )  # потом передавать хеш пассворд
            self.db.commit()
        except Exception as e:
            raise e
