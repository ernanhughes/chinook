import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_update_and_reset_items(client: AsyncClient) -> None:
    withnames = ['tracks', 'playlists', 'genres', 'mediatypes', 'artists', 'playlists']
    for endpoint in withnames:
        endpoint = f'/api/v1/{endpoint}/1'
        await check_update_key(client, endpoint, 'name', 'test_00001')
    albums_endpoint = f'/api/v1/albums/1'
    await check_update_key(client, albums_endpoint, 'title', 'test_00001')
    customers_endpoint = f'/api/v1/customers/1'
    await check_update_key(client, customers_endpoint, 'first_name', 'test_00001')
    employees_endpoint = f'/api/v1/employees/1'
    await check_update_key(client, employees_endpoint, 'first_name', 'test_00001')
    invoices_endpoint = f'/api/v1/invoices/1'
    await check_update_key(client, invoices_endpoint, 'total', 999999.99)
    invoice_items_endpoint = f'/api/v1/invoiceitems/1'
    await check_update_key(client, invoice_items_endpoint, 'quantity', 9999)
    # here I need to select a track that exists and update it with a track id that also exists
    playlist_tracks_endpoint = f'/api/v1/playlisttracks/1'
    await check_update_key(client, playlist_tracks_endpoint, 'track_id', 3389)


async def check_update_key(client: AsyncClient, endpoint: str, key: str, value: str) -> None:
    print(f'check_update_key: {endpoint} {key} {value}')
    # Make the GET request
    response = await client.get(endpoint)
    data = response.json()
    original_val = data[key]
    data[key] = value
    # Make the PUT request with the updated value
    response = await client.put(endpoint, json=data)
    assert response.status_code == 200
    print(f'Response from put: {response.json()}')
    response = await client.get(endpoint)
    updated_data = response.json()
    if updated_data[key] == value:
        print(f'Success: we updated the [{key} -> {updated_data[key]}] json: {updated_data}')
    else:
        print("Failed:", response.status_code)
    assert updated_data[key] == value
    # Reset the value
    updated_data[key] = original_val
    response = await client.put(endpoint, json=updated_data)
    assert response.status_code == 200
    print(f'Response from put: {response.json()}')
    response = await client.get(endpoint)
    reset_data = response.json()
    if original_val == reset_data[key]:
        print(f'Success: we reset the [{key} -> {reset_data[key]}] json: {reset_data}')
    else:
        print("Failed:", response.status_code)
    assert (original_val == reset_data[key])
