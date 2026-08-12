from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import Mock

from vienna_data_platform.services.wiener_linien import WienerLinienRawService


def test_fetch_and_store_traffic_info() -> None:
    data = (
        {
            "data": {
                "trafficInfos": [
                    {
                        "name": "I20260810-0028",
                        "title": "80A: Verkehrsunfall",
                    }
                ]
            },
            "message": {
                "value": "OK",
            },
        },
    )

    client = Mock()
    client.get_traffic_info.return_value = data

    storage = Mock()
    storage.build_raw_path.return_value = Path(
        "data/raw/wiener_linien/traffic_info/2026/08/10/20260810T180700Z.json"
    )

    service = WienerLinienRawService(client=client, storage=storage)

    timestamp = datetime(2026, 8, 10, 18, 7, 0, tzinfo=UTC)

    result = service.fetch_and_store_traffic_info(timestamp=timestamp)

    assert result == Path("data/raw/wiener_linien/traffic_info/2026/08/10/20260810T180700Z.json")

    client.get_traffic_info.assert_called_once_with()

    storage.build_raw_path.assert_called_once_with(
        source="wiener_linien",
        dataset="traffic_info",
        timestamp=timestamp,
    )

    storage.save_json.assert_called_once_with(data, result)
