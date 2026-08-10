from pathlib import Path

from vienna_data_platform.clients.wiener_linien import WienerLinienClient
from vienna_data_platform.services.raw_storage import RawStorageService


def test_wiener_linien_response_can_be_stored(tmp_path: Path) -> None:
    client = WienerLinienClient()
    storage = RawStorageService()

    # Fetch traffic information from Wiener Linien API
    traffic_info = client.get_traffic_info()

    # Define the path to store the JSON file
    path = tmp_path / "traffic_info.json"

    # Save the traffic information as a JSON file
    storage.save_json(traffic_info, path)

    # Verify that the file was created and contains the expected data
    assert path.exists()
