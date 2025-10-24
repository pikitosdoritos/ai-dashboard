from sqlalchemy import Integer, Column, String, DateTime, ForeignKey, Text
from backend.db.database import Base

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key = True)
    user = Column(Integer, nullable = False)
    task = Column(String, nullable = False)
    time = Column(Integer)
    status = Column(String, nullable = False)