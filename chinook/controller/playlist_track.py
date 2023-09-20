from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/playlisttracks/", tags=["playlisttracks"])
async def read_playlist_tracks():
    playlist_tracks = await prisma.playlisttrack.find_many()
    print("playlisttracks", playlist_tracks)
    return playlist_tracks


@router.get("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def read_playlist(playlist_id: int):
    print(f'Getting playlisttrack_id: {playlist_id}')
    playlist_track = await prisma.playlisttrack.find_unique(where={"id": playlist_id})
    return playlist_track
