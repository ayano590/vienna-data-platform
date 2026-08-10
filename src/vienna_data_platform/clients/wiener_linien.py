import requests


class WienerLinienClient:
    BASE_URL = "https://www.wienerlinien.at/ogd_realtime"

    def __init__(self, timeout: int = 10) -> None:
        self.timeout = timeout

    def get_traffic_info(self) -> dict:
        """
        Fetches traffic information from the Wiener Linien API.

        Returns:
            dict: A dictionary containing traffic information.
        """
        response = requests.get(
            f"{self.BASE_URL}/trafficInfoList",
            headers={"Accept": "application/json"},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()
