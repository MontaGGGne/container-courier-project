from app.dao.base import BaseDAO
from app.models import Locations


class LocationsDAO(BaseDAO):
    model = Locations
