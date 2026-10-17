from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_redirect():
    # Testa a criação do link
    response = client.post("/shorten", json={"url": "https://google.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_code" in data
    
    # Testa o redirecionamento
    short_code = data["short_code"]
    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://google.com/"