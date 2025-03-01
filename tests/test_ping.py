from fastapi.testclient import TestClient
from unittest.mock import patch

from api.main import app


client = TestClient(app)


def test_ping_url():
    with patch("aiohttp.ClientSession.get") as mock_get:
        # Настраиваем мок
        mock_get.return_value.__aenter__.return_value.status = 200
        mock_get.return_value.__aenter__.return_value.ok = True

        response = client.get(
            "/ping/",
            params=dict(
                url="https://google.com",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                }
        ))

        assert response.status_code == 200

        response_json = response.json()
        assert response_json == {
            "url": "https://google.com",
            "status": 200,
            "ok": True
        }