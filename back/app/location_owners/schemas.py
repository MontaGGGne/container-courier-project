from typing import Optional

from pydantic import BaseModel


class CCLocationOwners(BaseModel):
    owner_name: str

    class Config:
        from_attributes = True


class CULocationOwners(BaseModel):
    id: int
    owner_name: str = None
