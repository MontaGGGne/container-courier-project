from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models import Users
from app.users.dao import UsersDAO
from app.users.schemas import CUser, CUUser

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/create")
async def create(data: CUser, user: Users = Depends(get_current_user)):
    return await UsersDAO.create(data)


@router.get("/read")
async def read(user: Users = Depends(get_current_user)):
    return await UsersDAO.find_all()


@router.get("/read/{id}")
async def read_by_id(id: int, user: Users = Depends(get_current_user)):
    return await UsersDAO.find_one_or_none(id=id)


@router.delete("/delete/{id}")
async def delete_by_id(id: int, user: Users = Depends(get_current_user)):
    return await UsersDAO.delete(id)


@router.put("/update")
async def update(data: CUUser, user: Users = Depends(get_current_user)):
    return await UsersDAO.update(data)
