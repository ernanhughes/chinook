import logging

from fastapi import APIRouter
from prisma.partials import PlaylistPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/playlists/", tags=["playlists"])
async def read_playlists():
    playlists = await prisma.playlist.find_many()
    print("playlists", playlists)
    return playlists


@router.get("/playlists/{playlist_id}", tags=["playlists"])
async def read_playlist(playlist_id: int):
    logging.debug(f'Getting playlist id: {playlist_id}')
    try:
        playlist = await prisma.playlist.find_unique(where={"id": playlist_id})
    except Exception as e:
        logger.error(f'Exception while getting playlist {playlist_id}: {e}', e)
        raise e
    logging.debug(f'Found playlist: {playlist}')
    return playlist


@router.put("/playlists/{playlist_id}", tags=["playlists"])
async def update_playlist(playlist_id: int, playlist: PlaylistPostAndPut):
    logger.debug(f'Updating playlist_id: {playlist_id} with {playlist}')
    try:
        playlist = await prisma.playlist.update(data={"name": playlist.name},
                                                where={"id": playlist_id})
    except Exception as e:
        logger.error(f'Exception while updating playlist {playlist_id} with {playlist}: {e}', e)
        raise e
    logger.debug(f'Updated playlist {playlist}')
    return playlist


@router.post("/playlists/", tags=["playlists"])
async def create_playlist(playlist: PlaylistPostAndPut):
    logger.debug(f'Creating playlist {playlist}')
    try:
        playlist = await prisma.playlist.create(data={"name": playlist.name})
    except Exception as e:
        logger.error(f'Exception while creating new playlist {e}', e)
        raise e
    logger.debug(f'Created playlist {playlist}')
    return playlist


@router.delete("/playlists/{playlist_id}", tags=["playlists"])
async def delete_playlist(playlist_id: int):
    logger.info(f'Deleting playlist {playlist_id}')
    return await prisma.playlist.delete(where={"id": playlist_id})
