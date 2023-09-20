from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/artists/", tags=["artists"])
async def read_artists():
    artists = await prisma.artist.find_many()
    print("artists", artists)
    return artists


@router.get("/artists/{artist_id}", tags=["artists"])
async def read_artist(artist_id: int):
    print(f'Getting artist_id: {artist_id}')
    artist = await prisma.artist.find_unique(where={"ArtistId": artist_id})
    return artist
