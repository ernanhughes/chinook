import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_and_delete_items(client: AsyncClient) -> None:
    endpoints = ['albums', 'tracks', 'playlists', 'genres', 'mediatypes',
                 'artists', 'customers', 'employees', 'invoices', 'invoiceitems',
                 'playlisttracks']
    for endpoint in endpoints:
        await post_and_delete(client, f'/api/v1/{endpoint}/')


async def post_and_delete(client: AsyncClient, endpoint: str) -> None:
    print(f'post_and_delete: {endpoint}')
    # Make the GET request
    response = await client.get(endpoint)
    data = response.json()[1]
    del data["id"]  # remove the id field we will be posting this
    print(f'First item data in list: {data}')
    response = await client.post(endpoint, json=data)
    print(f'Response from post: {response.status_code} {response.json()}')
    if response.status_code == 200:
        print(f'Success: we posted data [{data} -> {response}')
    else:
        print("Failed:", response.status_code)
    assert response.status_code == 200
    created_id = response.json()['id']
    delete_endpoint = f'{endpoint}{created_id}'
    print(f'Delete endpoint: {delete_endpoint}')
    response = await client.delete(delete_endpoint)
    print(f'Response from delete: {response.status_code} {response.json()}')
    if response.status_code == 200:
        print(f'Success: we deleted data [{data} -> {response}')
    else:
        print("Failed:", response.status_code)
    assert response.status_code == 200
