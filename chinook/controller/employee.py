import logging

from fastapi import APIRouter
from prisma.partials import EmployeePostAndPut

from chinook.db.prisma import prisma

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/employees/", tags=["employees"])
async def read_employees():
    logging.debug("Getting employees")
    try:
        employees = await prisma.employee.find_many()
    except Exception as e:
        logger.error(f'Exception while getting employees: {e}', e)
        raise e
    logging.info(f"Found {employees.__len__()} employees")
    return employees


@router.get("/employees/{employee_id}", tags=["employees"])
async def read_employee(employee_id: int):
    logging.debug(f'Getting employee id: {employee_id}')
    try:
        employee = await prisma.employee.find_unique(where={"id": employee_id})
    except Exception as e:
        logger.error(f'Exception while getting employee {employee_id}: {e}', e)
        raise e
    logging.debug(f'Found employee: {employee}')
    return employee


@router.put("/employees/{employee_id}", tags=["employees"])
async def update_employee(employee_id: int, employee: EmployeePostAndPut):
    logger.debug(f'Updating employee_id: {employee_id} with {employee}')
    try:
        employee = await prisma.employee.update(
            data={"first_name": employee.first_name,
                  "last_name": employee.last_name,
                  "reports_to": employee.reports_to,
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
        logger.error(f'Exception while updating employee {employee_id} with {employee}: {e}', e)
        raise e
    logger.debug(f'Updated employee {employee}')
    return employee


@router.post("/employees/", tags=["employees"])
async def create_employee(employee: EmployeePostAndPut):
    logger.debug(f'Creating employee {employee}')
    try:
        employee = await prisma.employee.create(
            data={"first_name": employee.first_name,
                  "last_name": employee.last_name,
                  "reports_to": employee.reports_to,
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
        logger.error(f'Exception while creating new employee {e}', e)
        raise e
    logger.debug(f'Created employee {employee}')
    return employee


@router.delete("/employees/{employee_id}", tags=["employees"])
async def delete_employee(employee_id: int):
    logger.info(f'Deleting employee {employee_id}')
    return await prisma.employee.delete(where={"id": employee_id})
