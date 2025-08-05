from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)

    # Relaciones
    subjects = relationship(
        "Subject", back_populates="professor", cascade="all, delete"
    )
    enrollments = relationship(
        "Enrollment", back_populates="student", cascade="all, delete"
    )
