class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)     
        self.salary = salary
        
    def calculate_paycheck(self):
        return self.salary / 52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate, hours_worked):
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked
 
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, commission_rate, sales):
        super().__init__(fname, lname, salary)
        self.commission_rate = commission_rate
        self.sales = sales
        
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.commission_rate * self.sales
        return regular_salary + total_commission
