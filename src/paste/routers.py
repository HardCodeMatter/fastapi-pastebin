from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from .schemas import PasteCreate    
from .services import PasteService
from .exceptions import PasteAlreadyExist


router = APIRouter(
    prefix='/paste',
    tags=['Paste'],
)


@router.post('/create', response_model=PasteCreate)
async def create_paste(
    data: PasteCreate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        return await PasteService.create_paste(data, session)
    except PasteAlreadyExist as e:
        raise HTTPException(
            status_code=e.status_code,
            detail='Paste with this hash already exist.',
        )
