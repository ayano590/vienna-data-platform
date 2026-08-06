from prefect import flow

from vienna_data_platform.services.hello_service import get_message

@flow
def hello_flow():
    message = get_message()
    print(message)
