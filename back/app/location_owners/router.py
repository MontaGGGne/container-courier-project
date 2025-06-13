from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models import LocationOwners
from app.location_owners.dao import LocationOwnersDAO
from app.location_owners.schemas import CCLocationOwners, CULocationOwners

router = APIRouter(prefix="/location-owners", tags=["Компании владельцы"])


@router.post("/create")
async def create(data: CCLocationOwners):
    return await LocationOwnersDAO.create(data)


@router.get("/read")
async def read():
    return await LocationOwnersDAO.find_all()


@router.get("/read/{id}")
async def read_by_id(id: int):
    return await LocationOwnersDAO.find_one_or_none(id=id)


@router.delete("/delete/{id}")
async def delete_by_id(id: int):
    return await LocationOwnersDAO.delete(id)


@router.put("/update")
async def update(data: CULocationOwners):
    return await LocationOwnersDAO.update(data)
