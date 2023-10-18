import logging
from typing import List, Optional

from fastapi import APIRouter
from prisma.models import Employee
from prisma.partials import EmployeePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/employees/", tags=["employees"])
async def read_employees() -> List[Employee]:
    logger.debug("Getting employees")
    try:
        employees = await prisma.employee.find_many()
    except Exception as e:
        logger.error("Exception while getting employees: %s", e)
        raise e
    logger.info("Found %s employees", len(employees))
    return employees


@router.get("/employees/{employee_id}", tags=["employees"])
async def read_employee(employee_id: int) -> Optional[Employee]:
    logging.debug('Getting employee id: %s', employee_id)
    try:
        employee = await prisma.employee.find_unique(where={"id": employee_id})
    except Exception as e:
        logger.error('Exception while getting employee %s: %s', employee_id, e)
        raise e
    logging.debug('Found employee: %s', employee)
    return employee


@router.put("/employees/{employee_id}", tags=["employees"])
async def update_employee(employee_id: int, employee: EmployeePostAndPut) -> Optional[Employee]:
    logger.debug('Updating employee_id: %s with %s', employee_id, employee)
    try:
        employee = await prisma.employee.update(
            data={"first_name": employee.first_name,
                  "last_name": employee.last_name,
                  "reports_to_id": employee.reports_to_id,
                  "birth_date": employee.birth_date,
                  "hire_date": employee.hire_date,
                  "address": employee.address,
                  "city": employee.city,
                  "state": employee.state,
                  "country": employee.country,
                  "postal_code": employee.postal_code,
                  "phone": employee.phone,
                  "fax": employee.fax,
                  "email": employee.email},
            where={"id": employee_id})
    except Exception as e:
        logger.error('Exception while updating employee %s with %s: %s', employee_id, employee, e)
        raise e
    logger.debug('Updated employee %s', employee)
    return employee


@router.post("/employees/", tags=["employees"])
async def create_employee(employee: EmployeePostAndPut) -> Employee:
    logger.debug('Creating employee %s', employee)
    try:
        employee = await prisma.employee.create(
            data={"first_name": employee.first_name,
                  "last_name": employee.last_name,
                  "reports_to_id": employee.reports_to_id,
                  "birth_date": employee.birth_date,
                  "hire_date": employee.hire_date,
                  "address": employee.address,
                  "city": employee.city,
                  "state": employee.state,
                  "country": employee.country,
                  "postal_code": employee.postal_code,
                  "phone": employee.phone,
                  "fax": employee.fax,
                  "email": employee.email}
        )
    except Exception as e:
        logger.error('Exception while creating new employee %s', e)
        raise e
    logger.debug('Created employee %s', employee)
    return employee


@router.delete("/employees/{employee_id}", tags=["employees"])
async def delete_employee(employee_id: int) -> Optional[Employee]:
    logger.info('Deleting employee %s', employee_id)
    return await prisma.employee.delete(where={"id": employee_id})
