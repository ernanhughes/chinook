from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/invoiceitems/", tags=["invoiceitems"])
async def read_invoice_items():
    invoice_items = await prisma.invoiceitem.find_many()
    print("invoiceitems", invoice_items)
    return invoice_items


@router.get("/invoiceitems/{invoiceitem_id}", tags=["invoiceitems"])
async def read_invoice_item(invoice_item_id: int):
    print(f'Getting invoice_item_id: {invoice_item_id}')
    invoice_item = await prisma.invoiceitem.find_unique(where={"InvoiceLineId": invoice_item_id})
    return invoice_item
