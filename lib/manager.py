from lib.employee import Employee

class Manager:

    all_managers = []
    
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all_managers.append(self)

    @property
    def employees(self):
        return [e for e in Employee.all_employees if self == e.manager]
    
    @classmethod
    def all(cls):
        return cls.all_managers
    
    # def hire_employee(self, name, number):
    #     pass

    @classmethod
    def all_departments(cls):
        return [m.department for m in cls.all_managers]
    
    @classmethod
    def average_age(cls):
        age_list = [m.age for m in cls.all_managers]
        return float(sum(age_list) / len(age_list)) 