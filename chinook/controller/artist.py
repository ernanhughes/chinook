import logging
from typing import List, Optional

from fastapi import APIRouter
from prisma.models import Artist
from prisma.partials import ArtistPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/artists/", tags=["artists"])
async def read_artists() -> List[Artist]:
    logger.debug("Getting artists")
    try:
        artists = await prisma.artist.find_many()
    except Exception as e:
        logger.error('Exception while getting artists: %s', e)
        raise e
    logger.info("Found %s artists", len(artists))
    return artists


@router.get("/artists/{artist_id}", tags=["artists"])
async def read_artist(artist_id: int) -> Optional[Artist]:
    logging.debug('Getting artist_id: %s', artist_id)
    try:
        artist = await prisma.artist.find_unique(where={"id": artist_id})
    except Exception as e:
        logger.error('Exception while getting artist %s: %s', artist_id, e)
        raise e
    logging.debug('Found artist: %s', artist)
    return artist


@router.put("/artists/{artist_id}", tags=["artists"])
async def update_artist(artist_id: int, artist: ArtistPostAndPut) -> Optional[Artist]:
    logger.debug('Updating artist_id: %s with %s', artist_id, artist)
    try:
        artist = await prisma.artist.update(data={"name": artist.name},
                                            where={"id": artist_id})
    except Exception as e:
        logger.error('Exception while updating artist %s with %s: %s', artist_id, artist, e)
        raise e
    logger.debug('Updated artist %s', artist)
    return artist


@router.post("/artists/", tags=["artists"])
async def create_artist(artist: ArtistPostAndPut) -> Artist:
    logger.debug('Creating artist %s', artist)
    try:
        artist = await prisma.artist.create(data={"name": artist.name})
    except Exception as e:
        logger.error('Exception while creating new artist %s', e)
        raise e
    logger.debug('Created artist %s', artist)
    return artist


@router.delete("/artists/{artist_id}", tags=["artists"])
async def delete_artist(artist_id: int) -> Optional[Artist]:
    logger.info('Deleting artist %s', artist_id)
    return await prisma.artist.delete(where={"id": artist_id})
