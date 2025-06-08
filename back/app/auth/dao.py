from app.dao.base import BaseDAO
from app.models import Users


class AuthDAO(BaseDAO):
    model = Users
