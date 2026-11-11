from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_audit_report_success():
    response = client.get("/api/v1/students/770001/audit-report")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == "770001"
    assert "credit_summary" in data
    assert data["credit_summary"]["total_earned"] == 6

def test_student_not_found():
    response = client.get("/api/v1/students/999999/audit-report")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"
