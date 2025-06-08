from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.logic.dao import LogicDAO
from app.logic.schemas import CCOrder
from app.models import Users

router = APIRouter(prefix="/lc", tags=["Бизнес логика"])


@router.get("/ordersactive")
async def all_active_orders(user: Users = Depends(get_current_user)):
    return await LogicDAO.all_active_orders()


@router.get("/ordersin")
async def all_in_orders(user: Users = Depends(get_current_user)):
    return await LogicDAO.all_in_orders(user)


@router.post("/order/{id}")
async def take_order(id: int, user: Users = Depends(get_current_user)):
    return await LogicDAO.take_orders(id, user)


@router.post("/closeorders/{id}")
async def close_orders(id: int, user: Users = Depends(get_current_user)):
    return await LogicDAO.close_orders(id, user)


@router.get("/orders/{id}")
async def get_all_inf(id: int, user: Users = Depends(get_current_user)):
    return await LogicDAO.get_all_inf(id)


@router.get("/orderallinf/{id}")
async def get_prm_inf(id: int, user: Users = Depends(get_current_user)):
    return await LogicDAO.get_prm_inf(id)
