from employee import Employee




class Developer(Employee):
    def __init__(self,id: int,name: str ,base_salary: int,over_time: int,hourly_rate: int) -> None:
        super().__init__(id,name,base_salary)
        self.overtime_hours = over_time
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.base_salary + (self.overtime_hours * self.hourly_rate)


if __name__ == '__main__':
    d1 = Developer(1,'avi',8000,2,40)
    print(d1.employee_details())