from fastapi import APIRouter

from chinook.db.prisma import prisma

router = APIRouter()


@router.get("/employees/", tags=["employees"])
async def read_employees():
    employees = await prisma.employee.find_many()
    print("employees", employees)
    return employees


@router.get("/employees/{employee_id}", tags=["employees"])
async def read_employee(employee_id: int):
    print(f'Getting employee_id: {employee_id}')
    employee = await prisma.employee.find_unique(where={"employeeId": employee_id})
    return employee
