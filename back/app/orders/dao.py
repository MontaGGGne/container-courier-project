from app.dao.base import BaseDAO
from app.models import Orders


class OrdersDAO(BaseDAO):
    model = Orders
