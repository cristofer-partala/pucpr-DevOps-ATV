from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert "app" in response.json()

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "mensagem" in response.json()

def test_teste():
    response = client.get("/teste")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Rota de teste funcionando"

def test_rota_invalida():
    response = client.get("/rota_inexistente")
    assert response.status_code == 404

def test_info_conteudo():
    response = client.get("/info")
    data = response.json()
    assert data["app"] == "monitoramento"