from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = Field(default="development", min_length=1)
    app_host: str = Field(default="127.0.0.1", min_length=1)
    app_port: int = Field(default=8000, ge=1, le=65535)
    database_url: str = Field(
        default="sqlite:///./coloremotionstudy.db",
        min_length=1,
    )
    default_trial_count: int = Field(default=10)
    admin_api_token: str | None = None

    @field_validator("default_trial_count")
    @classmethod
    def validate_trial_count(cls, value: int) -> int:
        if value not in (10, 15):
            raise ValueError("DEFAULT_TRIAL_COUNT must be 10 or 15.")
        return value

    model_config = SettingsConfigDict(
        env_file=None,
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
