from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job......")


class Developer(Employee):

    def doJob(self):
        print("Write code....")

def BankJob(emp):   #polymorphism
    print("Bankjob Started".center(60, "-"))
    emp.doJob()
    print("Bankjob ended".center(60, "-"))
    print("-" * 60)

mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)

def BankJob(emps):   #polymorphism
    print("Bankjob Started".center(60, "-"))
    for emp in emps:
        emp.doJob()
    print("Bankjob ended".center(60, "-"))
    print("-" * 60)

BankJob([david, mike])