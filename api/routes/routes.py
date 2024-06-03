from fastapi import APIRouter
from api.routes.auth_routes import router as auth
from api.routes.fraud_routes import router as fraud_routes
from api.routes.user_routes import router as user_routes
from api.routes.dataset_routes import router as dataset_routes

routes = APIRouter()

routes.include_router(auth)
routes.include_router(user_routes, prefix='/api/users')
routes.include_router(dataset_routes, prefix='/dataset')
routes.include_router(fraud_routes, prefix='/api/is-fraud')