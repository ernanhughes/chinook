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
    print("playlisttracks", playlist_tracks)
    return playlist_tracks


@router.get("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def read_playlist_track(playlisttrack_id: int) -> Optional[PlaylistTrack]:
    logging.debug(f'Getting playlist track id: {playlisttrack_id}')
    try:
        playlist_track = await prisma.playlisttrack.find_unique(where={"id": playlisttrack_id})
    except Exception as e:
        logger.error(f'Exception while getting playlist track {playlisttrack_id}: {e}', e)
        raise e
    logging.debug(f'Found playlist track: {playlist_track}')
    return playlist_track


@router.put("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def update_playlist_track(pltrack_id: int, pltrack: PlaylistTrackPostAndPut) -> Optional[PlaylistTrack]:
    logger.debug(f'Updating playlisttrack_id: {pltrack_id} with {pltrack}')
    try:
        pltrack = await prisma.playlisttrack.update(
            data={"playlist_id": pltrack.playlist_id,
                  "track_id": pltrack.track_id},
            where={"id": pltrack_id})
    except Exception as e:
        logger.error(f'Exception while updating playlisttrack {pltrack_id} with {pltrack}: {e}', e)
        raise e
    logger.debug(f'Updated playlisttrack {pltrack}')
    return pltrack


@router.post("/playlisttracks/", tags=["playlisttracks"])
async def create_playlisttrack(playlisttrack: PlaylistTrackPostAndPut) -> PlaylistTrack:
    logger.debug(f'Creating playlist track {playlisttrack}')
    try:
        playlist_track = await prisma.playlisttrack.create(data={"playlist_id": playlisttrack.playlist_id,
                                                                 "track_id": playlisttrack.track_id})
    except Exception as e:
        logger.error(f'Exception while creating new playlist track {e}', e)
        raise e
    logger.debug(f'Created playlist track {playlist_track}')
    return playlist_track


@router.delete("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def delete_playlisttrack(playlisttrack_id: int) -> Optional[PlaylistTrack]:
    logger.info(f'Deleting playlisttrack {playlisttrack_id}')
    return await prisma.playlisttrack.delete(where={"id": playlisttrack_id})
