from typing import Optional

from pydantic import BaseModel


class CUser(BaseModel):
    email: str

    class Config:
        from_attributes = True


class CUUser(BaseModel):
    id: int
    email: Optional[str] = None
    code: Optional[str] = None

    class Config:
        from_attributes = True
