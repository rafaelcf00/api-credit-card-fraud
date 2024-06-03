import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

user = os.getenv("DATABASE_NAME")
port = os.getenv("DATABASE_PORT")
password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_DB_NAME")
host = os.getenv("DATABASE_HOST")

SQLALCHEMY_DATABASE_URL = f"postgresql://frauduser:1et00RD98zWykbsjSFWHO4K0mcc7roIS@dpg-cpf3s25ds78s7395pffg-a.oregon-postgres.render.com:5432/frauddb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
