import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import PlaylistTrack
from prisma.partials import PlaylistTrackPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/playlisttracks/", tags=["playlisttracks"])
async def read_playlist_tracks() -> List[PlaylistTrack]:
    playlist_tracks = await prisma.playlisttrack.find_many()
    logging.debug("playlisttracks %s", playlist_tracks)
    return playlist_tracks


@router.get("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def read_playlist_track(playlisttrack_id: int) -> Optional[PlaylistTrack]:
    logging.debug('Getting playlist track id: %s', playlisttrack_id)
    try:
        playlist_track = await prisma.playlisttrack.find_unique(where={"id": playlisttrack_id})
    except Exception as e:
        logger.error('Exception while getting playlist track %s: %s', playlisttrack_id, e)
        raise e
    logging.debug('Found playlist track: %s', playlist_track)
    return playlist_track


@router.put("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def update_playlist_track(pltrack_id: int, pltrack: PlaylistTrackPostAndPut) -> Optional[PlaylistTrack]:
    logger.debug('Updating playlisttrack_id: %s with %s', pltrack_id, pltrack)
    try:
        pltrack = await prisma.playlisttrack.update(
            data={"playlist_id": pltrack.playlist_id,
                  "track_id": pltrack.track_id},
            where={"id": pltrack_id})
    except Exception as e:
        logger.error('Exception while updating playlisttrack %s with %s: %s', pltrack_id, pltrack, e)
        raise e
    logger.debug('Updated playlisttrack %s', pltrack)
    return pltrack


@router.post("/playlisttracks/", tags=["playlisttracks"])
async def create_playlisttrack(playlisttrack: PlaylistTrackPostAndPut) -> PlaylistTrack:
    logger.debug('Creating playlist track %s', playlisttrack)
    try:
        playlist_track = await prisma.playlisttrack.create(data={"playlist_id": playlisttrack.playlist_id,
                                                                 "track_id": playlisttrack.track_id})
    except Exception as e:
        logger.error('Exception while creating new playlist track %s', e)
        raise e
    logger.debug('Created playlist track %s', playlist_track)
    return playlist_track


@router.delete("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def delete_playlisttrack(playlisttrack_id: int) -> Optional[PlaylistTrack]:
    logger.info('Deleting playlisttrack %s', playlisttrack_id)
    return await prisma.playlisttrack.delete(where={"id": playlisttrack_id})
