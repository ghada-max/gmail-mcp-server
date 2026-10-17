from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="GMAIL_MCP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    google_client_id: str
    google_client_secret: str
    google_refresh_token: str

def get_settings() -> Settings:
    return Settings()