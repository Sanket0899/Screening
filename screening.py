
# QNo-1=1. Create a function in python to read the text file and replace specific content
# of the file.
def file_replace(file_path,word_to_be_replaced,word_with_which_replaced):
    try:
        f=open(file_path,'r') # we opened the file in read mode
        data=f.read()
        data=data.replace(word_to_be_replaced,word_with_which_replaced) # replaced the content and stored in variable data
        f.close()
        f=open(file_path,'w') # now opened the file in write mode and written the data in the same file
        f.write(data)
        f.close()
    except Exception as e:
        print("No file present")


file_replace("C:/Users/sanaik/Music/FSDS Course/example.txt","placement","screening")

#===============================
# Qno-2
# Abstract method is a method which does not contain any implementation and the class containing the abstract
# method is called abstract class.Abstract class cannot be instantiated but we can inherit the abstract class.
# In python we have to use the ABC module to use the abstract class

# In the following example the Employee class is the abstract class and it is inerited by the Fulltime Employee
# and contract employee class

from abc import ABC,abstractmethod

class Employee_class(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee_class):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

class ContractEmployee(Employee_class):
    def __init__(self, first_name, last_name, no_of_days_worked, perday):
        super().__init__(first_name, last_name)
        self.no_of_days_worked = no_of_days_worked
        self.perday = perday

    def get_salary(self):
        return self.no_of_days_worked * self.perday

class Company:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")

company = Company()

company.add_employee(FulltimeEmployee('Sanket', 'Naik', 60000))
company.add_employee(ContractEmployee('Samarth', 'Naik', 1000, 15))
company.add_employee(ContractEmployee('XYZ', 'ZXY', 1500, 20))

company.print()

# -----------------------------------------

# Qno-3 Mulitple Inheritance
#
# It means two base class and one derived class

class Father():
    def Driving(self):
        print("Father Enjoys Driving")
class Mother():
    def Cooking(self):
        print("Mother Enjoys Cooking")
class Child(Father, Mother):
    def Playing(self):
        print("Child Loves Playing")
c = Child()
c.Driving()
c.Cooking()
c.Playing()

##Qno -4 Decorators
#Decorators is a tool in Python it allows to modify the behaviour of a function or class.

def hello_decorator(func):
    def inner1(a, b):
        print("Start decorator")
        # getting the returned value
        returned_value = func(a, b)
        print("after decorator")

        # returning the value to the original frame
        return returned_value

    return inner1

# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

print("Sum =", sum_two_numbers(a, b))

#Output will be
# Start decorator
# Inside the function
# after decorator
# Sum = 3
