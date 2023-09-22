import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_first_item(client: AsyncClient) -> None:
    endpoints = ['albums', 'tracks', 'playlists', 'genres', 'mediatypes',
                 'artists', 'customers', 'employees', 'invoices', 'invoiceitems',
                 'playlisttracks']
    for endpoint in endpoints:
        url = f'/api/v1/{endpoint}/1'
        print(url)
        # Make the GET request
        response = await client.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print(f'Failed: {url} {response.status_code}')
        assert response.status_code == 200
