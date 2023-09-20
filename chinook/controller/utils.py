from chinook.db.prisma import prisma


async def get_artist(album):
    return await prisma.artist.find_unique(where={"id": album.artist_id})
