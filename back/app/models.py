from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.sql import func

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    code = Column(String, nullable=True)
    if_staff = Column(Boolean, default=False)


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSON, nullable=True)
    address_start = Column(String, nullable=False)
    address_end = Column(String, nullable=False)
    comment = Column(String, nullable=True)

    user_id = Column(ForeignKey("users.id"), nullable=True)
    time_create = Column(DateTime, default=func.now())  # [not-callable]

    time_delivery = Column(Integer, nullable=True)

    time_start = Column(DateTime, nullable=True)
    time_end = Column(DateTime, nullable=True)

    price = Column(Integer, nullable=False)
    discount = Column(Float, nullable=True)

    type_payment = Column(String, default="Наличными")

    client = Column(String, nullable=False)

    client_number = Column(String, nullable=False)
    shop_name = Column(String, nullable=False)
