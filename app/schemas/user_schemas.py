from pydantic import BaseModel


# POST Регистрация request
class RegisterUser(BaseModel):
    username: str
    email: str
    password: str


# response 201 / GET
class ResponseUser(BaseModel):
    id: str
    username: str
    email: str
    role: str


# POST Логин request
class LoginUser(BaseModel):
    email: str
    password: str


# response 200
class LoginUserResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


# POST refresh request
class Refresh(BaseModel):
    refresh_token: str


# response
class RefreshResponse(BaseModel):
    access_token: str
    token_type: str


# POST logout Request
class LogoutUser(BaseModel):
    refresh_token: str


# response 204


# PATCH change_username Request
class ChangeUsername(BaseModel):
    username: str


# PATCH change_password Request
class ChangePassword(BaseModel):
    current_password: str
    new_password: str
