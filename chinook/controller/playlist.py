from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/playlists/", tags=["playlists"])
async def read_playlists():
    playlists = await prisma.playlist.find_many()
    print("playlists", playlists)
    return playlists


@router.get("/playlists/{playlist_id}", tags=["playlists"])
async def read_playlist(playlist_id: int):
    print(f'Getting playlist_id: {playlist_id}')
    playlist = await prisma.playlist.find_unique(where={"PlaylistId": playlist_id})
    return playlist
