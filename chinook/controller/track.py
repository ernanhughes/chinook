import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import Track
from prisma.partials import TrackPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/tracks/", tags=["tracks"])
async def read_tracks() -> List[Track]:
    tracks = await prisma.track.find_many()
    logging.debug("tracks %s", tracks)
    return tracks


@router.get("/tracks/{track_id}", tags=["tracks"])
async def read_track(track_id: int) -> Optional[Track]:
    logging.debug('Getting track id: %s', track_id)
    try:
        track = await prisma.track.find_unique(where={"id": track_id})
    except Exception as e:
        logger.error('Exception while getting track %s: %s', track_id, e)
        raise e
    logging.debug('Found track: %s', track)
    return track


@router.put("/tracks/{track_id}", tags=["tracks"])
async def update_track(track_id: int, track: TrackPostAndPut) -> Optional[Track]:
    logger.debug('Updating track_id: %s with %s', track_id, track)
    try:
        track = await prisma.track.update(
            data={"name": track.name,
                  "album_id": track.album_id,
                  "media_type_id": track.media_type_id,
                  "genre_id": track.genre_id,
                  "composer": track.composer,
                  "milliseconds": track.milliseconds,
                  "bytes": track.bytes,
                  "unit_price": track.unit_price},
            where={"id": track_id})
    except Exception as e:
        logger.error('Exception while updating track %s with %s: %s', track_id, track, e)
        raise e
    logger.debug('Updated track %s', track)
    return track


@router.post("/tracks/", tags=["tracks"])
async def create_track(track: TrackPostAndPut) -> Track:
    logger.debug('Creating track %s', track)
    try:
        track = await prisma.track.create(
            data={"name": track.name,
                  "album_id": track.album_id,
                  "media_type_id": track.media_type_id,
                  "genre_id": track.genre_id,
                  "composer": track.composer,
                  "milliseconds": track.milliseconds,
                  "bytes": track.bytes,
                  "unit_price": track.unit_price})
    except Exception as e:
        logger.error('Exception while creating new track %s', e)
        raise e
    logger.debug('Created track %s', track)
    return track


@router.delete("/tracks/{track_id}", tags=["tracks"])
async def delete_track(track_id: int) -> Optional[Track]:
    logger.info('Deleting track %s', track_id)
    return await prisma.track.delete(where={"id": track_id})
