import logging
from typing import Optional, List

from fastapi import APIRouter
from prisma.models import Invoice
from prisma.partials import InvoicePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/invoices/", tags=["invoices"])
async def read_invoices() -> List[Invoice]:
    logging.debug("Getting invoices")
    try:
        invoices = await prisma.invoice.find_many()
    except Exception as e:
        logger.error(f'Exception while getting invoices: {e}', e)
        raise e
    logging.info(f"Found {invoices.__len__()} invoices")
    return invoices


@router.get("/invoices/{invoice_id}", tags=["invoices"])
async def read_invoice(invoice_id: int) -> Optional[Invoice]:
    logging.debug(f'Getting invoice_id: {invoice_id}')
    try:
        invoice = await prisma.invoice.find_unique(where={"id": invoice_id})
    except Exception as e:
        logger.error(f'Exception while getting invoice {invoice_id}: {e}', e)
        raise e
    logging.debug(f'Found invoice: {invoice}')
    return invoice


@router.put("/invoices/{invoice_id}", tags=["invoices"])
async def update_invoice(invoice_id: int, invoice: InvoicePostAndPut) -> Optional[Invoice]:
    logger.debug(f'Updating invoice_id: {invoice_id} with {invoice}')
    try:
        invoice = await prisma.invoice.update(
            data={"customer_id": invoice.customer_id,
                  "invoice_date": invoice.invoice_date,
                  "billing_address": invoice.billing_address,
                  "billing_city": invoice.billing_city,
                  "billing_state": invoice.billing_state,
                  "billing_country": invoice.billing_country,
                  "billing_postal_code": invoice.billing_postal_code,
                  "total": invoice.total},
            where={"id": invoice_id})
    except Exception as e:
        logger.error(f'Exception while updating invoice {invoice_id} with {invoice}: {e}', e)
        raise e
    logger.debug(f'Updated invoice {invoice}')
    return invoice


@router.post("/invoices/", tags=["invoices"])
async def create_invoice(invoice: InvoicePostAndPut) -> Invoice:
    logger.debug(f'Creating invoice {invoice}')
    try:
        invoice = await prisma.invoice.create(data={"customer_id": invoice.customer_id,
                                                    "invoice_date": invoice.invoice_date,
                                                    "billing_address": invoice.billing_address,
                                                    "billing_city": invoice.billing_city,
                                                    "billing_state": invoice.billing_state,
                                                    "billing_country": invoice.billing_country,
                                                    "billing_postal_code": invoice.billing_postal_code,
                                                    "total": invoice.total})
    except Exception as e:
        logger.error(f'Exception while creating new invoice {e}', e)
        raise e
    logger.debug(f'Created invoice {invoice}')
    return invoice


@router.delete("/invoices/{invoice_id}", tags=["invoices"])
async def delete_invoice(invoice_id: int) -> Optional[Invoice]:
    logger.info(f'Deleting invoice {invoice_id}')
    return await prisma.invoice.delete(where={"id": invoice_id})
