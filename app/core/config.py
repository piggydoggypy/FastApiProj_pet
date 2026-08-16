from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    secret_key: str

def get_settings() -> Settings:
    return Settings(DATABASE_URL = "postgresql+psycopg://postgres:123456@127.0.0.1:5432/postgres",
                    secret_key='ewrdtfyvghbjnkmlDSDSGKLKDDSetrydtfgyvh')