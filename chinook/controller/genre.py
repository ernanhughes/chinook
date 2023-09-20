from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/genres/", tags=["genres"])
async def read_genres():
    genres = await prisma.genre.find_many()
    print("genres", genres)
    return genres


@router.get("/genres/{genre_id}", tags=["genres"])
async def read_genre(genre_id: int):
    print(f'Getting genre_id: {genre_id}')
    genre = await prisma.genre.find_unique(where={"GenreId": genre_id})
    return genre
