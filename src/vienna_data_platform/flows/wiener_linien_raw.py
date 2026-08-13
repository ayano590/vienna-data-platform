from pathlib import Path

from prefect import flow, get_run_logger

from vienna_data_platform.clients.wiener_linien import WienerLinienClient
from vienna_data_platform.services.raw_storage import RawStorageService
from vienna_data_platform.services.wiener_linien import WienerLinienRawService


@flow(
    name="wiener_linien_raw",
    description="Fetch Wiener Linien traffic information and store the raw API response.",
)
def wiener_linien_raw_flow() -> Path:
    client = WienerLinienClient()
    storage = RawStorageService()
    service = WienerLinienRawService(client=client, storage=storage)

    path = service.fetch_and_store_traffic_info()

    logger = get_run_logger()
    logger.info("Stored Wiener Linien traffic information at %s", path)

    return path


if __name__ == "__main__":
    wiener_linien_raw_flow()
