from src.database import Base
class boards(Base):
    __tablename__ = "Boards"
    id = Column(Integer, primary_key=True, autoincreament = True)
    title = Column(String(100), nullable=False)
    author = relationship("Users", back_populates="author", nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.mow())
    updated_at = пшеColumn(DateTime, server_default=func.mow(), onupdate=func.now())