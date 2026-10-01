
class Employee:

    def __init__(self, name, role, base_salary):
        self.name = name
        self.role = role
        self.base_salary = base_salary

    def calculate_salary(self):
        if self.role == "Manager":
            return self.base_salary * 1.5
        elif self.role == "Developer":
            return self.base_salary * 1.2
        else:
            return self.base_salary

    def save_to_file(self):
        with open("employee.txt", "w") as F:
            F.write(f"{emp1.name} who works as {emp1.role} gets salary of {emp1.calculate_salary()}")


emp1 = Employee("Jack", "Manager", 85000)
print(f"{emp1.name} who works as {emp1.role} gets salary of {emp1.calculate_salary()}")
emp1.save_to_file()









