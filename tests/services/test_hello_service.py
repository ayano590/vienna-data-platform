from vienna_data_platform.services.hello_service import get_message

def test_get_message():
    assert get_message() == "Hello from Prefect!"
