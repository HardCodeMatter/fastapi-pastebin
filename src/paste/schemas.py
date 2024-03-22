from pydantic import BaseModel, ConfigDict

from auth.schemas import UserRead


class PasteBase(BaseModel):
    hash: str
    uri: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class PasteCreate(PasteBase):
    user_id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class PasteRead(PasteBase):
    user: UserRead

    model_config = ConfigDict(
        from_attributes=True,
    )
