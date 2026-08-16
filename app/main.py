from contextlib import asynccontextmanager
from fastapi import FastAPI, status, Depends
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4

from app.schemas.user_schemas import (RegisterUser, ResponseUser, LoginUser, LoginUserResponse, Refresh, RefreshResponse,
                                      LogoutUser)

from app.models.models import Base
from app.db.session import engine

from app.api.routers.auth import router as auth_router
from app.api.routers.users import router as user_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(user_router)
# сделать middleware, сервис, бдшку, ядро с настрйоками


