from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env

def get_engine():
    db_url = f"{os.getenv('DB_TYPE')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}" \
             f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    return create_engine(db_url, echo=False)
