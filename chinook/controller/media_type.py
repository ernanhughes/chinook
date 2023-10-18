import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import MediaType
from prisma.partials import MediaTypePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/mediatypes/", tags=["mediatypes"])
async def read_mediatypes() -> List[MediaType]:
    logger.debug("Getting media types")
    try:
        mediatypes = await prisma.mediatype.find_many()
    except Exception as e:
        logger.error("Exception while getting mediatypes: %s", e)
        raise e
    logger.info("Found %s media types", len(mediatypes))
    return mediatypes


@router.get("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def read_mediatype(mediatype_id: int) -> Optional[MediaType]:
    logging.debug('Getting mediatype_id: %s', mediatype_id)
    try:
        mediatype = await prisma.mediatype.find_unique(where={"id": mediatype_id})
    except Exception as e:
        logger.error('Exception while getting mediatype %s: %s', mediatype_id, e)
        raise e
    logging.debug('Found mediatype: %s', mediatype)
    return mediatype


@router.put("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def update_mediatype(mt_id: int, mt: MediaTypePostAndPut) -> Optional[MediaType]:
    logger.debug('Updating mediatype_id: %s with %s', mt_id, mt)
    try:
        mt = await prisma.mediatype.update(data={"name": mt.name},
                                           where={"id": mt_id})
    except Exception as e:
        logger.error('Exception while updating mediatype %s with %s: %s',
                     mt_id, mt, e)
        raise e
    logger.debug('Updated mediatype %s', mt)
    return mt


@router.post("/mediatypes/", tags=["mediatypes"])
async def create_mediatype(mediatype: MediaTypePostAndPut) -> MediaType:
    logger.debug('Creating mediatype %s', mediatype)
    try:
        mediatype = await prisma.mediatype.create(data={"name": mediatype.name})
    except Exception as e:
        logger.error('Exception while creating new mediatype %s', e)
        raise e
    logger.debug('Created mediatype %s', mediatype)
    return mediatype


@router.delete("/mediatypes/{mediatype_id}", tags=["mediatypes"])
async def delete_mediatype(mediatype_id: int) -> Optional[MediaType]:
    logger.info('Deleting mediatype %s', mediatype_id)
    return await prisma.mediatype.delete(where={"id": mediatype_id})
