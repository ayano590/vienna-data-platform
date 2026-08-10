import json
from datetime import UTC, datetime
from pathlib import Path

from vienna_data_platform.services.raw_storage import RawStorageService


def test_save_json(tmp_path: Path) -> None:
    data = {
        "data": {"trafficInfos": [{"name": "I20260810-0028", "title": "80A: Verkehrsunfall"}]},
        "message": {"value": "OK"},
    }
    path = tmp_path / "traffic_info.json"

    service = RawStorageService()
    service.save_json(data, path)

    assert path.exists()

    with path.open(encoding="utf-8") as f:
        stored_data = json.load(f)

    assert stored_data == data


def test_build_raw_path() -> None:
    service = RawStorageService()

    timestamp = datetime(2026, 8, 10, 18, 7, 0, tzinfo=UTC)

    path = service.build_raw_path(
        source="wiener_linien", dataset="traffic_info", timestamp=timestamp
    )

    assert path == Path("data/raw/wiener_linien/traffic_info/2026/08/10/20260810T180700Z.json")
