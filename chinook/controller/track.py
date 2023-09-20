from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/tracks/", tags=["tracks"])
async def read_tracks():
    tracks = await prisma.track.find_many()
    print("tracks", tracks)
    return tracks


@router.get("/tracks/{track_id}", tags=["tracks"])
async def read_track(track_id: int):
    print(f'Getting track_id: {track_id}')
    track = await prisma.track.find_unique(where={"id": track_id})
    return track
