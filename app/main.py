from fastapi import FastAPI, HTTPException
from app.models import Tarea, TareaConId

app = FastAPI(title="Microservicio de Tareas", version="1.0.0")

# "Base de datos" en memoria (se reinicia cada vez que corres el servidor)
tareas_db: dict[int, TareaConId] = {}
contador_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Microservicio de Tareas funcionando correctamente"}


@app.get("/tareas", response_model=list[TareaConId])
def listar_tareas():
    return list(tareas_db.values())


@app.get("/tareas/{tarea_id}", response_model=TareaConId)
def obtener_tarea(tarea_id: int):
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas_db[tarea_id]


@app.post("/tareas", response_model=TareaConId, status_code=201)
def crear_tarea(tarea: Tarea):
    global contador_id
    nueva_tarea = TareaConId(id=contador_id, **tarea.model_dump())
    tareas_db[contador_id] = nueva_tarea
    contador_id += 1
    return nueva_tarea


@app.put("/tareas/{tarea_id}", response_model=TareaConId)
def actualizar_tarea(tarea_id: int, tarea: Tarea):
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_actualizada = TareaConId(id=tarea_id, **tarea.model_dump())
    tareas_db[tarea_id] = tarea_actualizada
    return tarea_actualizada


@app.delete("/tareas/{tarea_id}", status_code=204)
def eliminar_tarea(tarea_id: int):
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del tareas_db[tarea_id]
