import aiohttp
import ssl


def safe_url(url: str) -> str:
    if not url.startswith(('http://', 'https://')):
        return f'https://{url}'
    return url


async def ping(url: str, params: dict | None = None):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        async with aiohttp.ClientSession() as session:
            async with session.get(safe_url(url), params=params) as response:
                return {
                    'url': url,
                    'status': response.status,
                    'ok': response.ok,
                }
    except Exception as e:
        return {'error': str(e)}
