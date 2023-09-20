import logging

from fastapi import APIRouter
from prisma.partials import MediaTypePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/mediatypes/", tags=["mediatypes"])
async def read_mediatypes():
    logging.debug("Getting media types")
    try:
        mediatypes = await prisma.mediatype.find_many()
    except Exception as e:
        logger.error(f'Exception while getting mediatypes: {e}', e)
        raise e
    logging.info(f"Found {mediatypes.__len__()} media types")
    return mediatypes


@router.get("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def read_mediatype(mediatype_id: int):
    logging.debug(f'Getting mediatype_id: {mediatype_id}')
    try:
        mediatype = await prisma.mediatype.find_unique(where={"id": mediatype_id})
    except Exception as e:
        logger.error(f'Exception while getting mediatype {mediatype_id}: {e}', e)
        raise e
    logging.debug(f'Found mediatype: {mediatype}')
    return mediatype


@router.put("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def update_mediatype(mediatype_id: int, mediatype: MediaTypePostAndPut):
    logger.debug(f'Updating mediatype_id: {mediatype_id} with {mediatype}')
    try:
        mediatype = await prisma.mediatype.update(data={"name": mediatype.name},
                                                  where={"id": mediatype_id})
    except Exception as e:
        logger.error(f'Exception while updating mediatype {mediatype_id} with {mediatype}: {e}', e)
        raise e
    logger.debug(f'Updated mediatype {mediatype}')
    return mediatype


@router.post("/mediatypes/", tags=["mediatypes"])
async def create_mediatype(mediatype: MediaTypePostAndPut):
    logger.debug(f'Creating mediatype {mediatype}')
    try:
        mediatype = await prisma.mediatype.create(data={"name": mediatype.name})
    except Exception as e:
        logger.error(f'Exception while creating new mediatype {e}', e)
        raise e
    logger.debug(f'Created mediatype {mediatype}')
    return mediatype


@router.delete("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def delete_mediatype(mediatype_id: int):
    logger.info(f'Deleting mediatype {mediatype_id}')
    return await prisma.mediatype.delete(where={"id": mediatype_id})
