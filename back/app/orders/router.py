from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models import Users
from app.orders.dao import OrdersDAO
from app.orders.schemas import CCOrder, CUOrder

router = APIRouter(prefix="/orders", tags=["Заказы"])


@router.post("/create")
async def create(data: CCOrder, user: Users = Depends(get_current_user)):
    return await OrdersDAO.create(data)


@router.get("/read")
async def read(user: Users = Depends(get_current_user)):
    return await OrdersDAO.find_all()


@router.get("/read/{id}")
async def read_by_id(id: int, user: Users = Depends(get_current_user)):
    return await OrdersDAO.find_one_or_none(id=id)


@router.delete("/delete/{id}")
async def delete_by_id(id: int, user: Users = Depends(get_current_user)):
    return await OrdersDAO.delete(id)


@router.put("/update")
async def update(data: CUOrder, user: Users = Depends(get_current_user)):
    return await OrdersDAO.update(data)
