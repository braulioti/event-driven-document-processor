from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API
    app_name: str = Field(min_length=1)
    app_version: str = Field(min_length=1)
    app_env: Literal["development", "staging", "production"]
    api_host: str = Field(min_length=1)
    api_port: int = Field(ge=1, le=65535)
    api_reload: bool = False

    # Kafka
    kafka_bootstrap_servers: str = Field(min_length=1)
    kafka_document_topic: str = Field(min_length=1)
    kafka_consumer_group: str = Field(min_length=1)

    # AWS
    aws_region: str = Field(min_length=1)
    aws_access_key_id: str = Field(min_length=1)
    aws_secret_access_key: str = Field(min_length=1)
    aws_endpoint_url: str | None = None
    s3_bucket_name: str = Field(min_length=1)
    sqs_queue_name: str = Field(min_length=1)

    # Logging
    log_level: str = Field(min_length=1)
    log_format: str = Field(min_length=1)
    log_json: bool = False

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if normalized not in allowed:
            raise ValueError(f"log_level must be one of {', '.join(sorted(allowed))}")
        return normalized


@lru_cache
def get_settings() -> Settings:
    return Settings()
