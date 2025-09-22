import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the root .env file
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def test_connection():
    """
    Attempts to connect to the PostgreSQL database using environment variables.
    """
    print("\n🔍 Verifying DB connection details:")
    print("🔍 DB_NAME:", os.getenv("DB_NAME"))
    print("🔍 DB_USER:", os.getenv("DB_USER"))
    print("🔍 DB_HOST:", os.getenv("DB_HOST"))
    print("🔍 DB_PORT:", os.getenv("DB_PORT"))
    # print("🔍 DB_PASSWORD:", os.getenv("DB_PASSWORD"))

    print("\n📡 Attempting to connect to PostgreSQL...")

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        print(" Connected to PostgreSQL successfully!\n")
        conn.close()
    except Exception as e:
        print(f" Failed to connect to PostgreSQL: {e}\n")
