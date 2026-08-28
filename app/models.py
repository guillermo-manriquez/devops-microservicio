from pydantic import BaseModel
from typing import Optional

class Tarea(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

class TareaConId(Tarea):
    id: int