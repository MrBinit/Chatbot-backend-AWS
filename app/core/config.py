from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf_8"
    )

    APP_NAME: str
    ENV: str

    # Bedrock
    MODEL_ID: str
    MAXTOKEN: int
    TEMPERATURE: float
    TOPP: float
    AWS_REGION: str

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    # Auth
    AUTH_USERNAME: str
    AUTH_PASSWORD: str

settings = Settings()
