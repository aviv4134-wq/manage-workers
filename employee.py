

class Employee:


    def __int__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self.base_salary = base_salary

    def employee_details(self):
        return f'id : {self.id}\n name : {self.name}'

    def calculate_salary(self):
        return self.base_salary
     
        