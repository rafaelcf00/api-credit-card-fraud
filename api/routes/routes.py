from fastapi import APIRouter
from .auth_routes import router as auth
routes = APIRouter()

routes.include_router(auth)