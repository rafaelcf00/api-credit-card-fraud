from fastapi import APIRouter
from .auth_routes import router as auth
from .user_routes import router as user_routes

routes = APIRouter()

routes.include_router(auth)
routes.include_router(user_routes, prefix='/api/users')