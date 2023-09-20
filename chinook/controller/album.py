import logging

from fastapi import APIRouter
from prisma.partials import AlbumPostAndPut
from prisma.types import AlbumCreateInput

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/albums/", tags=["albums"])
async def read_albums():
    logger.info("Getting albums")
    albums = await prisma.album.find_many()
    logger.info("albums", albums)
    return albums


@router.get("/albums/{album_id}", tags=["albums"])
async def read_album(album_id: int):
    print(f'Getting album_id: {album_id}')
    album = await prisma.album.find_unique(where={"id": album_id})
    return album


@router.put("/albums/{album_id}", tags=["albums"])
async def update(album_id: int, album: AlbumPostAndPut):
    return await prisma.album.update(data={"title": album.Title, "artist_id": album.ArtistId},
                                     where={"id": album_id})


@router.post("/albums/", tags=["albums"])
async def post(album: AlbumPostAndPut):
    print("album", album)
    ip = AlbumCreateInput(Title=album.Title)
    print("ip", ip)
    try:
        album = await prisma.album.create(ip)
    except Exception as e:
        print("e", e)
        raise e
    print("album", album)
    return album


@router.delete("/albums/{album_id}", tags=["albums"])
async def delete(album_id: int):
    return await prisma.album.delete(where={"id": album_id})
