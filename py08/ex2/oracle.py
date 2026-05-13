from dotenv import load_dotenv
import os

load_dotenv()

matrix_mode = os.getenv("MATRIX_MODE")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")

variables: list = [
    matrix_mode,
    database_url,
    api_key,
    log_level,
    zion_endpoint,
]

required: list = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

missing: list = []

for i in variables:
    if i is None:
        missing.append(i)

if missing:
    print(f"Missing following configurations {missing}")


print(database_url)
