from fastapi import HTTPException, status


class PasteAlreadyExist(HTTPException):
    def __init__(self, status_code: int = status.HTTP_409_CONFLICT, detail: str | int | None = None) -> None:
        super().__init__(status_code, detail)
