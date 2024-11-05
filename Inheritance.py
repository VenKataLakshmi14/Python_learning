class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: ${self.salary}")

full_time_employee = FullTimeEmployee(101, "Alice", 50000)
full_time_employee.display_info()
