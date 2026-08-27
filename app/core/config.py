from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    secret_key: str
    cors_origins: list[str]


def get_settings() -> Settings:
    return Settings(
        DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db",
        secret_key="ewrdtfyvghbjnkmlDSDSGKLKDDSetrydtfgyvh",
        cors_origins=["http://localhost:3000"],
    )
