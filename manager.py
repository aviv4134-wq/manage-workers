from employee import Employee




class Manager(Employee):


    def __init__(self, id: int, name: str, base_salary: int, bonus:int):
        super().__init__(id, name, base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus

m1 = Manager(100,'bob',10000,1000)
if __name__ == '__main__':
   #print(m1.calculate_salary())
    
    pass