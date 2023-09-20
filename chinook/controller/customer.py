from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/customers/", tags=["customers"])
async def read_customers():
    customers = await prisma.customer.find_many()
    print("customers", customers)
    return customers


@router.get("/customers/{customer_id}", tags=["customers"])
async def read_customer(customer_id: int):
    print(f'Getting customer_id: {customer_id}')
    customer = await prisma.customer.find_unique(where={"CustomerId": customer_id})
    return customer
