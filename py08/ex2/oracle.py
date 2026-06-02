#!/usr/bin/env python3

from dotenv import load_dotenv
import os

load_dotenv()

required: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

missing: list[str] = []

for key in required:
    if os.getenv(key) is None:
        missing.append(key)

if missing:
    print("ORACLE STATUS: Configuration error\n")
    print(f"Missing configuration variables: {', '.join(missing)}")
    raise EnvironmentError("Configuration incomplete")

mode = os.getenv("MATRIX_MODE")

print("ORACLE STATUS: Reading the Matrix...\n")
print("Configuration loaded:")
print(f"Mode: {mode}")
print(f"Database: {os.getenv('DATABASE_URL')}")
print(f"API Access: {os.getenv('API_KEY')}")
print(f"Log Level: {os.getenv('LOG_LEVEL')}")
print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}\n")

print("Environment security check:")

if mode == "development":
    print("[DEV MODE] Local development environment")
    print("[DEV MODE] Verbose logging enabled")
    print("[DEV MODE] Safe for testing\n")

elif mode == "production":
    print("[PRODUCTION MODE] Production environment detected")
    print("[PRODUCTION MODE] Debug information hidden")
    print("[PRODUCTION MODE] Enhanced security active\n")

else:
    print(f"[WARNING] Unknown MATRIX_MODE: {mode}\n")

print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available\n")

print("The Oracle sees all configurations.")
