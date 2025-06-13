from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.logic.router import router as logic_router
from app.orders.router import router as orders_router
from app.users.router import router as users_router
from app.locations.router import router as locations_router
from app.location_owners.router import router as location_owners_router


app = FastAPI()

origins = [
    "*",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test():
    return "ok"


app.include_router(logic_router)
app.include_router(orders_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(locations_router)
app.include_router(location_owners_router)
