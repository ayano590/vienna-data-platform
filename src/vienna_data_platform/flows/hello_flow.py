from prefect import flow, get_run_logger

from vienna_data_platform.services.hello_service import get_message


@flow(name="hello_flow", description="A simple hello flow")
def hello_flow() -> None:
    message = get_message()
    logger = get_run_logger()
    logger.info(message)

if __name__ == "__main__":
    hello_flow()
