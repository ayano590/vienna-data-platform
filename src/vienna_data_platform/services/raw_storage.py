import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class RawStorageService:
    def build_raw_path(self, source: str, dataset: str, timestamp: datetime) -> Path:
        """
        Builds a file path for storing raw data based on the source, dataset, and timestamp.

        Args:
            source (str): The source of the data (e.g., "wiener_linien").
            dataset (str): The name of the dataset (e.g., "traffic_info").
            timestamp (Any): A datetime object representing the timestamp of the data.

        Returns:
            Path: The constructed file path.
        """

        timestamp_utc = timestamp.astimezone(UTC)
        return Path(
            f"data/raw/{source}/{dataset}/{timestamp_utc.strftime('%Y/%m/%d')}/{timestamp_utc.strftime('%Y%m%dT%H%M%SZ')}.json"
        )

    def save_json(self, data: Any, path: Path) -> None:
        """
        Saves the given data as a JSON file at the specified path.

        Args:
            data (Any): The data to be saved.
            path (Path): The path where the JSON file will be saved.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
