import logging

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)


async def get_artist(album):
    logger.debug(f'Getting artist for album: {album}')
    return await prisma.artist.find_unique(where={"id": album.artist_id})
