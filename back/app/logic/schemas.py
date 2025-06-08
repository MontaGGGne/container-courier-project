from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Json


class CCOrder(BaseModel):
    data: Optional[Json] = None
