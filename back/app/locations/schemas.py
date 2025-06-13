from typing import Optional

from pydantic import BaseModel


class CCLocation(BaseModel):
    address: str
    location_type: str
    location_owner_id: int
    description: str = None
    phone: str = None

    class Config:
        from_attributes = True


class CULocation(BaseModel):
    id: int
    address: str = None
    location_type: str = None
    location_owner_id: int = None
    description: str = None
    phone: str = None
