from fastapi import FastAPI
from app.routers import user_router, post_router, vote_router, authentication_router


app = FastAPI()

app.include_router(user_router.router)
app.include_router(post_router.router)
app.include_router(vote_router.router)
app.include_router(authentication_router.router)


@app.get("/")
async def roo():
    return {"mesagge": "¡Hola soy tu FastApi funcionando correctamente!"}

