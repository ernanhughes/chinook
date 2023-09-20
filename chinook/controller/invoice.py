from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/invoices/", tags=["invoices"])
async def read_invoices():
    invoices = await prisma.invoice.find_many()
    print("invoices", invoices)
    return invoices


@router.get("/invoices/{invoice_id}", tags=["invoices"])
async def read_invoice(invoice_id: int):
    print(f'Getting invoice_id: {invoice_id}')
    invoice = await prisma.invoice.find_unique(where={"id": invoice_id})
    return invoice
