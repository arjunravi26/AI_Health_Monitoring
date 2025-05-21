
from sqlalchemy import create_engine
from shared.config import DB_URL

def get_db_connection():
    return create_engine(DB_URL)
    