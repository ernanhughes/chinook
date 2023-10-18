import logging
from typing import List, Optional

from fastapi import APIRouter
from prisma.models import Album
from prisma.partials import AlbumPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/albums/", tags=["albums"])
async def read_albums() -> List[Album]:
    logger.debug("Getting albums")
    try:
        albums = await prisma.album.find_many()
    except Exception as e:
        logger.error('Exception while getting albums: %s', e)
        raise e
    logger.info("Found %s albums", len(albums))
    return albums


@router.get("/albums/{album_id}", tags=["albums"])
async def read_album(album_id: int) -> Optional[Album]:
    logging.debug('Getting album_id: %s', album_id)
    try:
        album = await prisma.album.find_unique(where={"id": album_id})
    except Exception as e:
        logger.error('Exception while getting album %s: %s', album_id, e)
        raise e
    logging.debug('Found Album: %s', album)
    return album


@router.put("/albums/{album_id}", tags=["albums"])
async def update_album(album_id: int, album: AlbumPostAndPut) -> Optional[Album]:
    logger.debug('Updating album_id: %s with %s', album_id, album)
    try:
        album = await prisma.album.update(
            data={"title": album.title, "artist_id": album.artist_id},
            where={"id": album_id})
    except Exception as e:
        logger.error('Exception while updating album %s with %s: %s', album_id, album, e)
        raise e
    logger.debug('Updated album %s', album)
    return album


@router.post("/albums/", tags=["albums"])
async def create_album(album: AlbumPostAndPut) -> Album:
    logger.debug('Creating album %s', album)
    try:
        album = await prisma.album.create(data={"title": album.title, "artist_id": album.artist_id})
    except Exception as e:
        logger.error('Exception while creating new album %s: %s', e, album)
        raise e
    logger.debug('Created album %s', album)
    return album


@router.delete("/albums/{album_id}", tags=["albums"])
async def delete_album(album_id: int) -> Optional[Album]:
    logger.info('Deleting album %s', album_id)
    return await prisma.album.delete(where={"id": album_id})
