from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = "Atlas API"
APP_DESCRIPTION = "AI Engineering Workspace Backend"
APP_VERSION = "0.1.0"

DATABASE_URL = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)