import pytest
from httpx import AsyncClient
from .utils import get_url


@pytest.mark.anyio
async def test_get_first_item(client: AsyncClient) -> None:
    endpoints = ['albums', 'tracks', 'playlists', 'genres', 'mediatypes',
                 'artists', 'customers', 'employees', 'invoices', 'invoiceitems',
                 'playlisttracks']
    for endpoint in endpoints:
        response = await get_url(client, f'/api/v1/{endpoint}/1')
        assert response.status_code == 200
