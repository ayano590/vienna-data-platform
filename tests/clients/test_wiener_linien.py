from unittest.mock import Mock, patch

import pytest
from requests.exceptions import HTTPError

from vienna_data_platform.clients.wiener_linien import WienerLinienClient


@patch("vienna_data_platform.clients.wiener_linien.requests.get")
def test_get_traffic_info(mock_get: Mock) -> None:
    response = Mock()
    response.json.return_value = {"data": {"trafficInfos": []}, "message": {"value": "OK"}}
    mock_get.return_value = response

    client = WienerLinienClient()
    result = client.get_traffic_info()

    assert result["message"]["value"] == "OK"
    assert result["data"]["trafficInfos"] == []

    mock_get.assert_called_once_with(
        "https://www.wienerlinien.at/ogd_realtime/trafficInfoList",
        headers={"Accept": "application/json"},
        timeout=10,
    )


@patch("vienna_data_platform.clients.wiener_linien.requests.get")
def test_get_traffic_info_http_error(mock_get: Mock) -> None:
    response = Mock()
    response.raise_for_status.side_effect = HTTPError("500 Server Error")
    mock_get.return_value = response

    client = WienerLinienClient()

    with pytest.raises(HTTPError):
        client.get_traffic_info()
