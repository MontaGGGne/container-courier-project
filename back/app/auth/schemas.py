from pydantic import BaseModel


class CMCode(BaseModel):
    email: str

    class Config:
        from_attributes = True


class CLogin(BaseModel):
    email: str
    code: str

    class Config:
        from_attributes = True


class CCode(BaseModel):
    id: int
    code: str
