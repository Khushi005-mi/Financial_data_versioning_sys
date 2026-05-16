from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql://postgres:password@localhost:5432/finos_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# THIS FUNCTION IS WHAT FASTAPI IS FAILING TO FIND
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()