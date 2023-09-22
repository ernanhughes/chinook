import logging

from fastapi import APIRouter
from prisma.partials import InvoiceItemPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/invoiceitems/", tags=["invoiceitems"])
async def read_invoice_items():
    logging.debug("Getting invoice items")
    try:
        invoice_items = await prisma.invoiceitem.find_many()
    except Exception as e:
        logger.error(f'Exception while getting invoice items: {e}', e)
        raise e
    logging.info(f"Found {invoice_items.__len__()} invoice items")
    return invoice_items


@router.get("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def read_invoiceitem(invoiceitem_id: int):
    logging.debug(f'Getting invoice item id: {invoiceitem_id}')
    try:
        invoice_item = await prisma.invoiceitem.find_unique(where={"id": invoiceitem_id})
    except Exception as e:
        logger.error(f'Exception while getting invoice item {invoiceitem_id}: {e}', e)
        raise e
    logging.debug(f'Found invoice item: {invoice_item}')
    return invoice_item


@router.put("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def update_invoiceitem(invoiceitem_id: int, invoiceitem: InvoiceItemPostAndPut):
    logger.debug(f'Updating invoice item id: {invoiceitem_id} with {invoiceitem}')
    try:
        invoice_item = await prisma.invoiceitem.update(data={
            "invoice_id": invoiceitem.invoice_id,
            "track_id": invoiceitem.track_id,
            "unit_price": invoiceitem.unit_price,
            "quantity": invoiceitem.quantity},
            where={"id": invoiceitem_id})
    except Exception as e:
        logger.error(f'Exception while updating invoice item {invoiceitem_id} with {invoiceitem}: {e}', e)
        raise e
    logger.debug(f'Updated invoice item {invoice_item}')
    return invoice_item


@router.post("/invoiceitems/", tags=["invoiceitems"])
async def create_invoiceitem(invoiceitem: InvoiceItemPostAndPut):
    logger.debug(f'Creating invoice item {invoiceitem}')
    try:
        invoice_item = await prisma.invoiceitem.create(data={
            "invoice_id": invoiceitem.invoice_id,
            "track_id": invoiceitem.track_id,
            "unit_price": invoiceitem.unit_price,
            "quantity": invoiceitem.quantity})
    except Exception as e:
        logger.error(f'Exception while creating new invoice item {e}', e)
        raise e
    logger.debug(f'Created invoice item {invoice_item}')
    return invoice_item


@router.delete("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def delete_invoiceitem(invoiceitem_id: int):
    logger.info(f'Deleting invoice item {invoiceitem_id}')
    return await prisma.invoiceitem.delete(where={"id": invoiceitem_id})
