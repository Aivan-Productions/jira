from sqlalchemy import Integer, String, ForeignKey, DateTime, func, Column
from sqlalchemy.orm import relationship
from src.database import Base
class Boards(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    author = relationship("Users", back_populates="author")
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)