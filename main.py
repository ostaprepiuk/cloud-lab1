from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class FeedSchedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(String, index=True)
    portion_size = Column(Integer)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pet Feeder API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/schedules")
def get_schedules(db: Session = Depends(get_db)):
    return db.query(FeedSchedule).all()
