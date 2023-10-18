import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import Playlist
from prisma.partials import PlaylistPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/playlists/", tags=["playlists"])
async def read_playlists() -> List[Playlist]:
    playlists = await prisma.playlist.find_many()
    logging.debug("playlists %s", playlists)
    return playlists


@router.get("/playlists/{playlist_id}", tags=["playlists"])
async def read_playlist(playlist_id: int) -> Optional[Playlist]:
    logging.debug('Getting playlist id: %s', playlist_id)
    try:
        playlist = await prisma.playlist.find_unique(where={"id": playlist_id})
    except Exception as e:
        logger.error('Exception while getting playlist %s: %s', playlist_id, e)
        raise e
    logging.debug('Found playlist: %s', playlist)
    return playlist


@router.put("/playlists/{playlist_id}", tags=["playlists"])
async def update_playlist(playlist_id: int, playlist: PlaylistPostAndPut) -> Optional[Playlist]:
    logger.debug('Updating playlist_id: %s with %s', playlist_id, playlist)
    try:
        playlist = await prisma.playlist.update(data={"name": playlist.name},
                                                where={"id": playlist_id})
    except Exception as e:
        logger.error('Exception while updating playlist %s with %s: %s', playlist_id, playlist, e)
        raise e
    logger.debug('Updated playlist %s', playlist)
    return playlist


@router.post("/playlists/", tags=["playlists"])
async def create_playlist(playlist: PlaylistPostAndPut) -> Playlist:
    logger.debug('Creating playlist %s', playlist)
    try:
        playlist = await prisma.playlist.create(data={"name": playlist.name})
    except Exception as e:
        logger.error('Exception while creating new playlist %s', e)
        raise e
    logger.debug('Created playlist %s', playlist)
    return playlist


@router.delete("/playlists/{playlist_id}", tags=["playlists"])
async def delete_playlist(playlist_id: int) -> Optional[Playlist]:
    logger.info('Deleting playlist %s', playlist_id)
    return await prisma.playlist.delete(where={"id": playlist_id})
