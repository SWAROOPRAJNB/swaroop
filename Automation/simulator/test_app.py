import pytest 
from app import app
 
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
 
def test_get_quipment(client):
    response = client.get("/api/equipment")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) ==2
    # [{"id":101,"name":"Flight","status":"Operational","type":"FCU"},
    #  {"id":102,"name":"Navigational System","status":"Operational","type":"NS"}]
    assert data[0]["id"] == 101
    assert data[0]["name"] == "Flight Control Unit"
    assert data[0]["status"] == "operational"
    assert data[0]["type"] == "FCU"