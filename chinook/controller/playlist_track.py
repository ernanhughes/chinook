import logging

from fastapi import APIRouter
from prisma.partials import PlaylistTrackPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/playlisttracks/", tags=["playlisttracks"])
async def read_playlist_tracks():
    playlist_tracks = await prisma.playlisttrack.find_many()
    print("playlisttracks", playlist_tracks)
    return playlist_tracks


@router.get("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def read_playlist_track(playlisttrack_id: int):
    logging.debug(f'Getting playlist track id: {playlisttrack_id}')
    try:
        playlist_track = await prisma.playlisttrack.find_unique(where={"id": playlisttrack_id})
    except Exception as e:
        logger.error(f'Exception while getting playlist track {playlisttrack_id}: {e}', e)
        raise e
    logging.debug(f'Found playlist track: {playlist_track}')
    return playlist_track


@router.put("/playlisttracks/{playlisttrack_id}", tags=["playlisttracks"])
async def update_playlist_track(playlisttrack_id: int, playlisttrack: PlaylistTrackPostAndPut):
    logger.debug(f'Updating playlisttrack_id: {playlisttrack_id} with {playlisttrack}')
    try:
        playlisttrack = await prisma.playlisttrack.update(
            data={"playlist_id": playlisttrack.playlist_id,
                  "track_id": playlisttrack.track_id},
            where={"id": playlisttrack_id})
    except Exception as e:
        logger.error(f'Exception while updating playlisttrack {playlisttrack_id} with {playlisttrack}: {e}', e)
        raise e
    logger.debug(f'Updated playlisttrack {playlisttrack}')
    return playlisttrack


@router.post("/playlisttracks/", tags=["playlisttracks"])
async def create_playlisttrack(playlisttrack: PlaylistTrackPostAndPut):
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
async def delete_playlisttrack(playlisttrack_id: int):
    logger.info(f'Deleting playlisttrack {playlisttrack_id}')
    return await prisma.playlisttrack.delete(where={"id": playlisttrack_id})
