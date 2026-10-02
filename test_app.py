from app import app
def home1():
    client=app.test_client()
    v=client.get('/')
    assert v.status_code==200
    assert v.data==b"sai"