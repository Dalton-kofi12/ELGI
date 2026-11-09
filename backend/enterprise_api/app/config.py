import os
from dataclasses import dataclass


def get_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.lower() in ("true", "1", "yes", "on")


@dataclass(frozen=True)
class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "ELGI Enterprise API"
    )

    APP_VERSION: str = os.getenv(
        "APP_VERSION",
        "0.2.0"
    )

    ENVIRONMENT: str = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DEBUG: bool = get_bool("DEBUG", False)

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./elgi_enterprise.db"
    )

    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        ""
    )

    ALLOWED_ORIGINS: tuple = tuple(
        origin.strip()
        for origin in os.getenv(
            "ALLOWED_ORIGINS",
            "http://localhost:3000,http://localhost:5173"
        ).split(",")
        if origin.strip()
    )


settings = Settings()
