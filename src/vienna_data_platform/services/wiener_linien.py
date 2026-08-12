from datetime import UTC, datetime
from pathlib import Path

from vienna_data_platform.clients.wiener_linien import WienerLinienClient
from vienna_data_platform.services.raw_storage import RawStorageService


class WienerLinienRawService:
    def __init__(
        self,
        client: WienerLinienClient,
        storage: RawStorageService,
    ) -> None:
        self.client = client
        self.storage = storage

    def fetch_and_store_traffic_info(
        self,
        timestamp: datetime | None = None,
    ) -> Path:
        """
        Fetches traffic information from the Wiener Linien API and stores it as a JSON file.

        Args:
            timestamp (datetime | None): The timestamp to use for the filename. If None, the current UTC time is used.

        Returns:
            Path: The path to the stored JSON file.
        """
        # Fetch traffic information from Wiener Linien API
        traffic_info = self.client.get_traffic_info()

        # Use the provided timestamp or the current UTC time if None
        if timestamp is None:
            timestamp = datetime.now(UTC)

        # Define the path to store the JSON file with a timestamped filename
        path = self.storage.build_raw_path(
            source="wiener_linien",
            dataset="traffic_info",
            timestamp=timestamp,
        )

        # Save the traffic information as a JSON file
        self.storage.save_json(traffic_info, path)

        return path
