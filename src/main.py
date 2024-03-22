import uvicorn
from fastapi import FastAPI

from auth.routers import router as auth_router
from paste.routers import router as paste_router


app = FastAPI(
    title='Pastebin API',
    version='0.1.0',
)

app.include_router(auth_router)
app.include_router(paste_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
