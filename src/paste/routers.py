from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from .schemas import PasteCreate    
from .services import PasteService


router = APIRouter(
    prefix='/paste',
    tags=['Paste'],
)


@router.post('/create', response_model=PasteCreate)
async def create_paste(
    data: PasteCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await PasteService.create_paste(data, session)
