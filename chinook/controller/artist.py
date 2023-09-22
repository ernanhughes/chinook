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
    logging.debug("Getting artists")
    try:
        artists = await prisma.artist.find_many()
    except Exception as e:
        logger.error(f'Exception while getting artists: {e}', e)
        raise e
    logging.info(f"Found {artists.__len__()} artists")
    return artists


@router.get("/artists/{artist_id}", tags=["artists"])
async def read_artist(artist_id: int) -> Optional[Artist]:
    logging.debug(f'Getting artist_id: {artist_id}')
    try:
        artist = await prisma.artist.find_unique(where={"id": artist_id})
    except Exception as e:
        logger.error(f'Exception while getting artist {artist_id}: {e}', e)
        raise e
    logging.debug(f'Found artist: {artist}')
    return artist


@router.put("/artists/{artist_id}", tags=["artists"])
async def update_artist(artist_id: int, artist: ArtistPostAndPut) -> Optional[Artist]:
    logger.debug(f'Updating artist_id: {artist_id} with {artist}')
    try:
        artist = await prisma.artist.update(data={"name": artist.name},
                                            where={"id": artist_id})
    except Exception as e:
        logger.error(f'Exception while updating artist {artist_id} with {artist}: {e}', e)
        raise e
    logger.debug(f'Updated artist {artist}')
    return artist


@router.post("/artists/", tags=["artists"])
async def create_artist(artist: ArtistPostAndPut) -> Artist:
    logger.debug(f'Creating artist {artist}')
    try:
        artist = await prisma.artist.create(data={"name": artist.name})
    except Exception as e:
        logger.error(f'Exception while creating new artist {e}', e)
        raise e
    logger.debug(f'Created artist {artist}')
    return artist


@router.delete("/artists/{artist_id}", tags=["artists"])
async def delete_artist(artist_id: int) -> Optional[Artist]:
    logger.info(f'Deleting artist {artist_id}')
    return await prisma.artist.delete(where={"id": artist_id})
