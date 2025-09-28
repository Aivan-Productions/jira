from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Board(Base):
    __tablename__ = "Boards"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = relationship("Users", back_populates="author", nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)