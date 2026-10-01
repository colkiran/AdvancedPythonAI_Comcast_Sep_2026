
class Employee:
    def __init__(self, name, role, base_salary):
        self.name = name
        self.role = role
        self.base_salary = base_salary

class SalaryCalculator:
    def calculate(self, employee: Employee):
        if employee.role == "Manager":
            return employee.base_salary * 1.5
        elif employee.role == "Developer":
            return employee.base_salary * 1.2
        else:
            return employee.base_salary


class EmployeeRepository:
    def save(self, employee: Employee, salcalc: SalaryCalculator):
        with open("employee.txt", "w") as F:
            F.write(f"{employee.name} who works as {employee.role} gets salary of {salcalc.calculate(employee)}")

emp1 = Employee("Micheal", "Developer", 78500)

salcalc = SalaryCalculator()
print(salcalc.calculate(emp1))

rep = EmployeeRepository()
rep.save(emp1, salcalc)


