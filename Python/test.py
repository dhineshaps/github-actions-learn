from py_flask import app

def test_home():
    # Test the home route
    response = app.test_client().get("/")
    
    assert response.status_code==200  # Check for HTTP 200 status
