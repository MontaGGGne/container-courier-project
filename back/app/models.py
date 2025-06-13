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
    Enum
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

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

    location_id = Column(ForeignKey("locations.id", ondelete='CASCADE'), nullable=True)

    address_end = Column(String, nullable=False)
    comment = Column(String, nullable=True)

    user_id = Column(ForeignKey("users.id", ondelete='CASCADE'), nullable=True)

    time_create = Column(DateTime, default=func.now())  # [not-callable]
    time_delivery = Column(Integer, nullable=True)
    time_start = Column(DateTime, nullable=True)
    time_end = Column(DateTime, nullable=True)
    price = Column(Integer, nullable=False)
    discount = Column(Float, nullable=True)
    type_payment = Column(String, default="Наличными")
    client = Column(String, nullable=False)
    client_number = Column(String, nullable=False)


class Locations(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, nullable=False)
    location_type = Column(String, nullable=False)
    location_owner_id = Column(ForeignKey("location_owners.id", ondelete='CASCADE'), nullable=False)
    description = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class LocationOwners(Base):
    __tablename__ = "location_owners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_name = Column(String, unique=True, index=True, nullable=False)
