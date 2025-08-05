from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import user
from sqlalchemy import text

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema Educativo API",
    description="API para gestionar profesores, alumnos y materias",
    version="1.0.0",
)


# Ruta de prueba
@app.get("/")
async def root():
    """Ruta de bienvenida."""
    return {"message": "¡Bienvenido al Sistema Educativo API!"}


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


# Ruta para obtener todos los usuarios (temporal, para probar)
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    """Obtener todos los usuarios (solo para testing)."""
    users = db.query(user.User).all()
    return {
        "users": [
            {"id": u.id, "name": u.name, "email": u.email, "role": u.role.value}
            for u in users
        ]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
