from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_listar_tareas_vacio():
    response = client.get("/tareas")
    assert response.status_code == 200


def test_crear_tarea():
    response = client.post("/tareas", json={"titulo": "Estudiar DevOps"})
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Estudiar DevOps"
    assert data["completada"] is False
    assert "id" in data


def test_obtener_tarea():
    crear = client.post("/tareas", json={"titulo": "Tarea de prueba"})
    tarea_id = crear.json()["id"]

    response = client.get(f"/tareas/{tarea_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarea de prueba"


def test_obtener_tarea_inexistente():
    response = client.get("/tareas/9999")
    assert response.status_code == 404


def test_actualizar_tarea():
    crear = client.post("/tareas", json={"titulo": "Original"})
    tarea_id = crear.json()["id"]

    response = client.put(
        f"/tareas/{tarea_id}",
        json={"titulo": "Actualizada", "completada": True}
    )
    assert response.status_code == 200
    assert response.json()["titulo"] == "Actualizada"
    assert response.json()["completada"] is True


def test_eliminar_tarea():
    crear = client.post("/tareas", json={"titulo": "Para borrar"})
    tarea_id = crear.json()["id"]

    response = client.delete(f"/tareas/{tarea_id}")
    assert response.status_code == 204

    response = client.get(f"/tareas/{tarea_id}")
    assert response.status_code == 404

def test_obtener_estadisticas():
    response = client.get("/stats")
    assert response.status_code == 200
    assert "total_tareas" in response.json()