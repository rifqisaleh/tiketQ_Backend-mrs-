def test_create_ticket(client):
    response = client.post("/tickets/", json={
        "event_name": "Test Ticket",
        "location": "Jakarta",
        "time": "2025-08-10T19:00:00"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["event_name"] == "Test Ticket"
    assert data["is_used"] is False

def test_get_all_tickets(client):
    # Create two tickets first
    client.post("/tickets/", json={
        "event_name": "Event A",
        "location": "Jakarta",
        "time": "2025-08-10T10:00:00"
    })

    client.post("/tickets/", json={
        "event_name": "Event B",
        "location": "Singapore",
        "time": "2025-08-11T11:00:00"
    })

    # Test GET
    response = client.get("/tickets/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2

def test_get_ticket_by_id(client):
    create_response = client.post("/tickets/", json={
        "event_name": "Event X",
        "location": "Bali",
        "time": "2025-08-12T12:00:00"
    })
    ticket = create_response.get_json()
    ticket_id = ticket["id"]

    get_response = client.get(f"/tickets/{ticket_id}")
    assert get_response.status_code == 200
    data = get_response.get_json()
    assert data["id"] == ticket_id
    assert data["event_name"] == "Event X"

def test_patch_ticket_as_used(client):
    res = client.post("/tickets/", json={
        "event_name": "Patch Test",
        "location": "Medan",
        "time": "2025-08-13T15:00:00"
    })
    ticket_id = res.get_json()["id"]

    patch_res = client.patch(f"/tickets/{ticket_id}")
    assert patch_res.status_code == 200
    data = patch_res.get_json()
    assert data["is_used"] is True

def test_delete_ticket(client):
    res = client.post("/tickets/", json={
        "event_name": "Delete Test",
        "location": "Surabaya",
        "time": "2025-08-14T17:00:00"
    })
    ticket_id = res.get_json()["id"]

    del_res = client.delete(f"/tickets/{ticket_id}")
    assert del_res.status_code == 200
    assert del_res.get_json()["message"] == "Ticket deleted successfully"

    # Confirm it's really gone
    followup = client.get(f"/tickets/{ticket_id}")
    assert followup.status_code == 404
