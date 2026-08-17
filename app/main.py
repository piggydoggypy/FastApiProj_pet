from fastapi import FastAPI, Request, Response
from time import perf_counter
import logging
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.auth import router as auth_router
from app.api.routers.users import router as user_router
from app.core.logging_settings import configure_logging
from app.core.config import get_settings

configure_logging()


# @asynccontextmanager
# async def lifespan(_: FastAPI):
#     # Base.metadata.create_all(bind=engine)
#     yield

# app = FastAPI(lifespan=lifespan)
settings = get_settings()
app = FastAPI()
logger = logging.getLogger("app.middleware")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.middleware("http")  # log_requests выполнится до и после обработки каждого HTTP-запроса
async def log_requests(request: Request, call_next) -> Response:
    started_at = perf_counter()
    try:
        response: Response = await call_next(request)  # Работа самого эндпоинта
    except Exception:
        duration_ms = (perf_counter() - started_at) * 1000
        logger.exception(
            "Request failed: %s %s completed_in=%.2fms",
            request.method,
            request.url.path,
            duration_ms,
        )
        raise

    duration_ms = (perf_counter() - started_at) * 1000
    logger.info(
        "%s %s -> %s (%.2f ms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


# middleware для подсчёта количества реквестов, добавил логированние для удобства
count = 0
@app.middleware("http")
async def count_requests(request: Request, call_next) -> Response:
    global count
    response: Response = await call_next(request)
    count +=1
    response.headers["X-Request-Number"] = str(count)
    logger.info(
        "%s %s -> %s requests_count %s",
        request.method,
        request.url.path,
        response.status_code,
        count,
    )


    return response

app.include_router(auth_router)
app.include_router(user_router)


