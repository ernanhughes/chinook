import logging

from fastapi import APIRouter
from prisma.partials import GenrePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/genres/", tags=["genres"])
async def read_genres():
    logging.debug("Getting genres")
    try:
        genres = await prisma.genre.find_many()
    except Exception as e:
        logger.error(f'Exception while getting genres: {e}', e)
        raise e
    logging.info(f"Found {genres.__len__()} genres")
    return genres


@router.get("/genres/{genre_id}", tags=["genres"])
async def read_genre(genre_id: int):
    logging.debug(f'Getting genre_id: {genre_id}')
    try:
        genre = await prisma.genre.find_unique(where={"id": genre_id})
    except Exception as e:
        logger.error(f'Exception while getting genre {genre_id}: {e}', e)
        raise e
    logging.debug(f'Found genre: {genre}')
    return genre


@router.put("/genres/{genre_id}", tags=["genres"])
async def update_genre(genre_id: int, genre: GenrePostAndPut):
    logger.debug(f'Updating genre_id: {genre_id} with {genre}')
    try:
        genre = await prisma.genre.update(data={"name": genre.name},
                                          where={"id": genre_id})
    except Exception as e:
        logger.error(f'Exception while updating genre {genre_id} with {genre}: {e}', e)
        raise e
    logger.debug(f'Updated genre {genre}')
    return genre


@router.post("/genres/", tags=["genres"])
async def create_genre(genre: GenrePostAndPut):
    logger.debug(f'Creating genre {genre}')
    try:
        genre = await prisma.genre.create(data={"name": genre.name})
    except Exception as e:
        logger.error(f'Exception while creating new genre {e}', e)
        raise e
    logger.debug(f'Created genre {genre}')
    return genre


@router.delete("/genres/{genre_id}", tags=["genres"])
async def delete_genre(genre_id: int):
    logger.info(f'Deleting genre {genre_id}')
    return await prisma.genre.delete(where={"id": genre_id})
