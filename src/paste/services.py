from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from .schemas import PasteCreate
from .models import Paste
from .exceptions import PasteAlreadyExist


class PasteService:
    @staticmethod
    async def create_paste(data: PasteCreate, session: AsyncSession):
        paste = await session.execute(
            select(Paste).filter(Paste.hash == data.hash)
        )
        if paste.first():
            raise PasteAlreadyExist()

        new_paste = Paste(**data.model_dump())

        session.add(new_paste)
        await session.commit()

        return new_paste
