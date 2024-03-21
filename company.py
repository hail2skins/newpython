from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print("Employees:")
        for employee in self.employees:
            print(f"{employee.fname} {employee.lname}")
        print('----------------')
        
    def pay_employees(self):
        print("Paychecks:")
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('____________')
        
def main():
    my_company = Company()
    
    employee1 = SalaryEmployee("John", "Doe", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Jane", "Doe", 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee("Jim", "Doe", 30000, 5, 200)
    my_company.add_employee(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()
main()