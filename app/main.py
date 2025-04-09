from fastapi import FastAPI
from app.routers import user_router


app = FastAPI()

app.include_router(user_router.router)

print("✅ main.py loaded desde app.main")

@app.get("/")
async def roo():
    return {"mesagge": "¡Hola soy tu FastApi funcionando correctamente!"}

