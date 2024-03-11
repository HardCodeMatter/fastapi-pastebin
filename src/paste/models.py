import typing
from datetime import datetime
from sqlalchemy import ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
if typing.TYPE_CHECKING:
    from auth.models import User


class Paste(Base):
    __tablename__ = 'paste'

    hash: Mapped[str] = mapped_column(String(6), primary_key=True, unique=True, index=True)
    uri: Mapped[str] = mapped_column(String(256), unique=True)

    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    expired_at: Mapped[datetime] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(back_populates='pastes')
