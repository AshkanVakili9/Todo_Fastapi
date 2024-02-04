from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# DATABASE_URL = 'postgresql://postgres:araa23o385@localhost/TodoApplicationDatabase'
DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
