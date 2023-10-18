import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import InvoiceItem
from prisma.partials import InvoiceItemPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/invoiceitems/", tags=["invoiceitems"])
async def read_invoice_items() -> List[InvoiceItem]:
    logger.debug("Getting invoice items")
    try:
        invoice_items = await prisma.invoiceitem.find_many()
    except Exception as e:
        logger.error("Exception while getting invoice items: %s", e)
        raise e
    logger.info("Found %s invoice items", len(invoice_items))
    return invoice_items


@router.get("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def read_invoiceitem(invoiceitem_id: int) -> Optional[InvoiceItem]:
    logging.debug('Getting invoice item id: %s', invoiceitem_id)
    try:
        invoice_item = await prisma.invoiceitem.find_unique(where={"id": invoiceitem_id})
    except Exception as e:
        logger.error('Exception while getting invoice item %s: %s', invoiceitem_id, e)
        raise e
    logging.debug('Found invoice item: %s', invoice_item)
    return invoice_item


@router.put("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def update_invoiceitem(invoiceitem_id: int, invoiceitem: InvoiceItemPostAndPut) -> Optional[InvoiceItem]:
    logger.debug('Updating invoice item id: %s with %s', invoiceitem_id, invoiceitem)
    try:
        invoice_item = await prisma.invoiceitem.update(data={
            "invoice_id": invoiceitem.invoice_id,
            "track_id": invoiceitem.track_id,
            "unit_price": invoiceitem.unit_price,
            "quantity": invoiceitem.quantity},
            where={"id": invoiceitem_id})
    except Exception as e:
        logger.error('Exception while updating invoice item %s with %s: %s', invoiceitem_id, invoiceitem, e)
        raise e
    logger.debug('Updated invoice item %s', invoice_item)
    return invoice_item


@router.post("/invoiceitems/", tags=["invoiceitems"])
async def create_invoiceitem(invoiceitem: InvoiceItemPostAndPut) -> InvoiceItem:
    logger.debug('Creating invoice item %s', invoiceitem)
    try:
        invoice_item = await prisma.invoiceitem.create(data={
            "invoice_id": invoiceitem.invoice_id,
            "track_id": invoiceitem.track_id,
            "unit_price": invoiceitem.unit_price,
            "quantity": invoiceitem.quantity})
    except Exception as e:
        logger.error('Exception while creating new invoice item %s', e)
        raise e
    logger.debug('Created invoice item %s', invoice_item)
    return invoice_item


@router.delete("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def delete_invoiceitem(invoiceitem_id: int) -> Optional[InvoiceItem]:
    logger.info('Deleting invoice item %s', invoiceitem_id)
    return await prisma.invoiceitem.delete(where={"id": invoiceitem_id})
