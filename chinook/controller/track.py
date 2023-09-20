import logging

from fastapi import APIRouter
from prisma.partials import TrackPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/tracks/", tags=["tracks"])
async def read_tracks():
    tracks = await prisma.track.find_many()
    print("tracks", tracks)
    return tracks


@router.get("/tracks/{track_id}", tags=["tracks"])
async def read_track(track_id: int):
    logging.debug(f'Getting track id: {track_id}')
    try:
        track = await prisma.track.find_unique(where={"id": track_id})
    except Exception as e:
        logger.error(f'Exception while getting track {track_id}: {e}', e)
        raise e
    logging.debug(f'Found track: {track}')
    return track


@router.put("/tracks/{track_id}", tags=["tracks"])
async def update_track(track_id: int, track: TrackPostAndPut):
    logger.debug(f'Updating track_id: {track_id} with {track}')
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
        logger.error(f'Exception while updating track {track_id} with {track}: {e}', e)
        raise e
    logger.debug(f'Updated track {track}')
    return track


@router.post("/tracks/", tags=["tracks"])
async def create_track(track: TrackPostAndPut):
    logger.debug(f'Creating track {track}')
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
        logger.error(f'Exception while creating new track {e}', e)
        raise e
    logger.debug(f'Created track {track}')
    return track


@router.delete("/tracks/{track_id}", tags=["tracks"])
async def delete_track(track_id: int):
    logger.info(f'Deleting track {track_id}')
    return await prisma.track.delete(where={"id": track_id})
