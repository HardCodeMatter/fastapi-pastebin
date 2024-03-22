from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import PasteCreate
from .models import Paste


class PasteService:
    @staticmethod
    async def create_paste(data: PasteCreate, session: AsyncSession):
        try:
            paste = Paste(**data.model_dump())

            session.add(paste)
            await session.commit()

            return paste
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
