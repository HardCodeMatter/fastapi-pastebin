from fastapi import APIRouter, Depends

from .models import User
from .schemas import UserCreate, UserRead
from .manager import auth_backend, current_active_user, fastapi_users


router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/jwt',
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router.include_router(
    fastapi_users.get_reset_password_router(),
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


@router.get('/authenticated-route')
async def authenticated_route(user: User = Depends(current_active_user)):
    return {'message': f'Hello, welcome back, {user.username}[{user.id}].'}
