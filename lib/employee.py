class Employee:
    all_employees = []
    
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all_employees.append(self)

    @classmethod
    def all(cls):
        return [e for e in cls.all_employees]
    
    @classmethod
    def paid_over(cls,number):
        return [e for e in cls.all_employees if e.salary > number]\
        
    @classmethod
    def find_by_department(cls, department_string):
        for e in cls.all_employees:
            if e.manager.department == department_string:
                return e.name
                break

    def tax_bracket(self):
        return [e for e in Employee.all_employees if e.salary in range((self.salary-1000), (self.salary+1000))]