from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "OCR Backend"
    tesseract_cmd: str = "tesseract"

    class Config:
        env_file = ".env"

settings = Settings()
