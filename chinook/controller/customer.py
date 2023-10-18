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
    logger.debug("Getting customers")
    try:
        customers = await prisma.customer.find_many()
    except Exception as e:
        logger.error("Exception while getting customers: %s", e)
        raise e
    logger.info("Found %d customers", len(customers))
    return customers


@router.get("/customers/{customer_id}", tags=["customers"])
async def read_customer(customer_id: int) -> Optional[Customer]:
    logging.debug('Getting customer id: %s', customer_id)
    try:
        customer = await prisma.customer.find_unique(where={"id": customer_id})
    except Exception as e:
        logger.error('Exception while getting customer %s: %s', customer_id, e)
        raise e
    logging.debug('Found customer: %s', customer)
    return customer


@router.put("/customers/{customer_id}", tags=["customers"])
async def update_customer(customer_id: int, customer: CustomerPostAndPut) -> Optional[Customer]:
    logger.debug('Updating customer_id: %s with %s', customer_id, customer)
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
        logger.error('Exception while updating customer %s with %s: %s', customer_id, customer, e)
        raise e
    logger.debug('Updated customer %s', customer)
    return customer


@router.post("/customers/", tags=["customers"])
async def create_customer(customer: CustomerPostAndPut) -> Customer:
    logger.debug('Creating customer %s', customer)
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
        logger.error('Exception while creating new customer %s', e)
        raise e
    logger.debug('Created customer %s', customer)
    return customer


@router.delete("/customers/{customer_id}", tags=["customers"])
async def delete_customer(customer_id: int) -> Optional[Customer]:
    logger.info('Deleting customer %s', customer_id)
    return await prisma.customer.delete(where={"id": customer_id})
