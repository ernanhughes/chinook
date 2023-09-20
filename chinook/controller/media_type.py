from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/mediatypes/", tags=["mediatypes"])
async def read_mediatypes():
    mediatypes = await prisma.mediatype.find_many()
    print("mediatypes", mediatypes)
    return mediatypes


@router.get("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def read_mediatype(mediatype_id: int):
    print(f'Getting mediatype_id: {mediatype_id}')
    mediatype = await prisma.mediatype.find_unique(where={"MediaTypeId": mediatype_id})
    return mediatype
