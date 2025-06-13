from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Json


class CCOrder(BaseModel):
    data: Optional[Json] = None
    address_end: str
    comment: Optional[str] = None
    price: int
    discount: Optional[float] = None
    type_payment: Optional[str] = None
    client: str
    client_number: str

    class Config:
        from_attributes = True


class CUOrder(BaseModel):
    id: int
    user_id: Optional[int] = None
    time_delivery: Optional[int] = None
    time_start: Optional[datetime] = None
    time_end: Optional[datetime] = None
    type_payment: Optional[str] = None
