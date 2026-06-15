

class Employee:


    def __init__(self,id: int,name: str,base_salary : int):
        self.id = id
        self.name = name
        self.base_salary = base_salary

    def employee_details(self):
        return f'id : {self.id}\n name : {self.name}'

    def calculate_salary(self):
        return self.base_salary
     
        