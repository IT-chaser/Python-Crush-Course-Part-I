class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.firs_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_salary='$5,000'):
        self.annual_salary = annual_salary
        return self.annual_salary
