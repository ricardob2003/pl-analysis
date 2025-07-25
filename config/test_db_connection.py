import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

load_dotenv()
print(env_path)
print("🔍 DB_NAME:", os.getenv("DB_NAME"))
print("🔍 DB_USER:", os.getenv("DB_USER"))
print("🔍 DB_PASS:", os.getenv("DB_PASS"))
print("🔍 DB_HOST:", os.getenv("DB_HOST"))
print("🔍 DB_PORT:", os.getenv("DB_PORT"))

print (" Attempting to Connect to PostgreSQL...")

try:
    conn = psycopg2.connect(
        print("Connecting to PostgreSQL database..."),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    print(" Connected to PostgreSQL successfully!")
    conn.close()
except Exception as e:
    print(f"This is the error message: Failed to connect to PostgreSQL: {e}")
