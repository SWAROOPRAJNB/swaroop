from dataclasses import dataclass

@dataclass
class Employee:

    employee_id: int
    employee_name: str
    department: str

employee=Employee(101,"aditya","airbs")

print(employee)
print(employee.employee_name)
