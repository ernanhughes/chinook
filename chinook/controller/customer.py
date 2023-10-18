import logging
from typing import Optional

from fastapi import APIRouter
from prisma.models import Customer
from prisma.partials import CustomerPostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/customers/", tags=["customers"])
async def read_customers() -> list[Customer]:
    logging.debug("Getting customers")
    try:
        customers = await prisma.customer.find_many()
    except Exception as e:
        logger.error(f'Exception while getting customers: {e}', e)
        raise e
    logging.info(f"Found {customers.__len__()} customers")
    return customers


@router.get("/customers/{customer_id}", tags=["customers"])
async def read_customer(customer_id: int) -> Optional[Customer]:
    logging.debug(f'Getting customer id: {customer_id}')
    try:
        customer = await prisma.customer.find_unique(where={"id": customer_id})
    except Exception as e:
        logger.error(f'Exception while getting customer {customer_id}: {e}', e)
        raise e
    logging.debug(f'Found customer: {customer}')
    return customer


@router.put("/customers/{customer_id}", tags=["customers"])
async def update_customer(customer_id: int, customer: CustomerPostAndPut) -> Optional[Customer]:
    logger.debug(f'Updating customer_id: {customer_id} with {customer}')
    try:
        customer = await prisma.customer.update(
            data={"first_name": customer.first_name,
                  "last_name": customer.last_name,
                  "company": customer.company,
                  "address": customer.address,
                  "city": customer.city,
                  "state": customer.state,
                  "country": customer.country,
                  "postal_code": customer.postal_code,
                  "phone": customer.phone,
                  "fax": customer.fax,
                  "email": customer.email,
                  "support_rep_id": customer.support_rep_id},
            where={"id": customer_id})
    except Exception as e:
        logger.error(f'Exception while updating customer {customer_id} with {customer}: {e}', e)
        raise e
    logger.debug(f'Updated customer {customer}')
    return customer


@router.post("/customers/", tags=["customers"])
async def create_customer(customer: CustomerPostAndPut) -> Customer:
    logger.debug(f'Creating customer {customer}')
    try:
        customer = await prisma.customer.create(
            data={"first_name": customer.first_name,
                  "last_name": customer.last_name,
                  "company": customer.company,
                  "address": customer.address,
                  "city": customer.city,
                  "state": customer.state,
                  "country": customer.country,
                  "postal_code": customer.postal_code,
                  "phone": customer.phone,
                  "fax": customer.fax,
                  "email": customer.email,
                  "support_rep_id": customer.support_rep_id})
    except Exception as e:
        logger.error(f'Exception while creating new customer {e}', e)
        raise e
    logger.debug(f'Created customer {customer}')
    return customer


@router.delete("/customers/{customer_id}", tags=["customers"])
async def delete_customer(customer_id: int) -> Optional[Customer]:
    logger.info(f'Deleting customer {customer_id}')
    return await prisma.customer.delete(where={"id": customer_id})
