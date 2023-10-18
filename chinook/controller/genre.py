import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import Genre
from prisma.partials import GenrePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/genres/", tags=["genres"])
async def read_genres() -> List[Genre]:
    logger.debug("Getting genres")
    try:
        genres = await prisma.genre.find_many()
    except Exception as e:
        logger.error('Exception while getting genres: %s', e)
        raise e
    logger.info("Found %s genres", len(genres))
    return genres


@router.get("/genres/{genre_id}", tags=["genres"])
async def read_genre(genre_id: int) -> Optional[Genre]:
    logging.debug('Getting genre_id: %s', genre_id)
    try:
        genre = await prisma.genre.find_unique(where={"id": genre_id})
    except Exception as e:
        logger.error('Exception while getting genre %s: %s', genre_id, e)
        raise e
    logging.debug('Found genre: %s', genre)
    return genre


@router.put("/genres/{genre_id}", tags=["genres"])
async def update_genre(genre_id: int, genre: GenrePostAndPut) -> Optional[Genre]:
    logger.debug('Updating genre_id: %s with %s', genre_id, genre)
    try:
        genre = await prisma.genre.update(data={"name": genre.name},
                                          where={"id": genre_id})
    except Exception as e:
        logger.error('Exception while updating genre %s with %s: %s', genre_id, genre, e)
        raise e
    logger.debug('Updated genre %s', genre)
    return genre


@router.post("/genres/", tags=["genres"])
async def create_genre(genre: GenrePostAndPut) -> Genre:
    logger.debug('Creating genre %s', genre)
    try:
        genre = await prisma.genre.create(data={"name": genre.name})
    except Exception as e:
        logger.error('Exception while creating new genre %s: %s', e, genre)
        raise e
    logger.debug('Created genre %s', genre)
    return genre


@router.delete("/genres/{genre_id}", tags=["genres"])
async def delete_genre(genre_id: int) -> Optional[Genre]:
    logger.info('Deleting genre %s', genre_id)
    return await prisma.genre.delete(where={"id": genre_id})
