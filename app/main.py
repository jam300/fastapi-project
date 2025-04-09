from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from app.database import engine

app = FastAPI()

@app.get("/check-db")
def check_db_connection():
    try:
        with engine.connect() as conn:
            return {"status": "✅ Conexión exitosa a SQL Server"}
    except SQLAlchemyError as e:
        return {"error": str(e)}

@app.get("/")
async def roo():
    return {"mesagge": "¡Hola soy tu FastApi funcionando correctamente!"}