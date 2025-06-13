from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models import Locations
from app.locations.dao import LocationsDAO
from app.locations.schemas import CCLocation, CULocation

router = APIRouter(prefix="/locations", tags=["Локации"])


@router.post("/create")
async def create(data: CCLocation):
    return await LocationsDAO.create(data)


@router.get("/read")
async def read():
    return await LocationsDAO.find_all()


@router.get("/read/{id}")
async def read_by_id(id: int):
    return await LocationsDAO.find_one_or_none(id=id)


@router.delete("/delete/{id}")
async def delete_by_id(id: int):
    return await LocationsDAO.delete(id)


@router.put("/update")
async def update(data: CULocation):
    return await LocationsDAO.update(data)
