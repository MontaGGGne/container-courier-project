from app.dao.base import BaseDAO
from app.models import LocationOwners


class LocationOwnersDAO(BaseDAO):
    model = LocationOwners
