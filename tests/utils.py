from httpx import AsyncClient
from starlette.responses import Response


async def get_url(client: AsyncClient, url: str) -> Response:
    print(url)
    # Make the GET request
    response = await client.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print(f'Failed: {url} {response.status_code}')
    return response
