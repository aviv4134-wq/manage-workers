from manager import Manager,m1
from developer import Developer,d1


class Company:

    def __init__(self):
        self.workers = []

    def add_worker(self,worker :object):
        self.workers.append(worker)

    def show_all_workers(self):
        for worker in self.workers:
            print(worker.employee_details())

    def sum_salary(self):
        sum_salary = 0
        for worker in self.workers:
            sum_salary += worker.calculate_salary()
        return sum_salary

    def show_worker_by_id(self,id):
        for worker in self.workers:
            if worker.id == id:
                return worker.employee_details()
        return 'employee not exists'

    def delete_employee(self,id):
        for worker in self.workers:
            if worker.id == id:
                self.workers.remove(worker)
                return None

    def generate_payroll_report(self):
        for worker in self.workers:
            salary = worker.calculate_salary()
            id = worker.id
            name = worker.name
            worker_type = type(worker).__name__
            print(f'name:{name} worker type: {worker_type} salary {salary} ')
                
            


if __name__ == '__main__':
   com = Company()
   com.add_worker(m1)
   com.add_worker(d1)
#    print(com.workers)
#    com.show_all_workers()
#    print(com.sum_salary())
   print(com.show_worker_by_id(1))
   com.delete_employee(1)
   print(com.show_worker_by_id(1))
   com.generate_payroll_report()