from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import os


DB_CONFIG = {
    "drivername": os.environ.get("DB_DRIVERNAME", "postgresql"),
    "username": os.environ.get("DB_USERNAME", "username"),
    "password": os.environ.get("DB_PASSWORD", "password"),
    "host": os.environ.get("DB_HOST", "postgres"),
    "port": os.environ.get("DB_PORT", "5432"),
    "database": os.environ.get("DB_DATABASE", "dbname"),
}

DATABASE_URL = str(URL(**DB_CONFIG))
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)
