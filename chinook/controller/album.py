import logging

from fastapi import APIRouter
from prisma.partials import AlbumPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/albums/", tags=["albums"])
async def read_albums():
    logging.debug("Getting albums")
    try:
        albums = await prisma.album.find_many()
    except Exception as e:
        logger.error(f'Exception while getting albums: {e}', e)
        raise e
    logging.info(f"Found {albums.__len__()} albums")
    return albums


@router.get("/albums/{album_id}", tags=["albums"])
async def read_album(album_id: int):
    logging.debug(f'Getting album_id: {album_id}')
    try:
        album = await prisma.album.find_unique(where={"id": album_id})
    except Exception as e:
        logger.error(f'Exception while getting album {album_id}: {e}', e)
        raise e
    logging.debug(f'Found Album: {album}')
    return album


@router.put("/albums/{album_id}", tags=["albums"])
async def update_album(album_id: int, album: AlbumPostAndPut):
    logger.debug(f'Updating album_id: {album_id} with {album}')
    try:
        album = await prisma.album.update(
            data={"title": album.title, "artist_id": album.artist_id},
            where={"id": album_id})
    except Exception as e:
        logger.error(f'Exception while updating album {album_id} with {album}: {e}', e)
        raise e
    logger.debug(f'Updated album {album}')
    return album


@router.post("/albums/", tags=["albums"])
async def create_album(album: AlbumPostAndPut):
    logger.debug(f'Creating album {album}')
    try:
        album = await prisma.album.create(data={"title": album.title, "artist_id": album.artist_id})
    except Exception as e:
        logger.error(f'Exception while creating new album {e}', e)
        raise e
    logger.debug(f'Created album {album}')
    return album


@router.delete("/albums/{album_id}", tags=["albums"])
async def delete_album(album_id: int):
    logger.info(f'Deleting album {album_id}')
    return await prisma.album.delete(where={"id": album_id})
