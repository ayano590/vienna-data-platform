from unittest.mock import Mock, patch

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
