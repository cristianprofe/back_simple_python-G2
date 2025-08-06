from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import user
from sqlalchemy import text
from app.api.routes import user


# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema Educativo API",
    description="API para gestionar profesores, alumnos y materias",
    version="1.0.0",
)


# Ruta para probar la conexión a la base de datos
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Verificar el estado de la aplicación y la base de datos."""
    try:
        # Intentar hacer una consulta simple
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "message": "La aplicación está funcionando correctamente",
        }
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}


app.include_router(user.router)
