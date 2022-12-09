# Oops -- Object Oriented Programmings.

# class -- blue print of an object. 

# object -- Instance of a class.



"""
class Classname:
    statements
"""

# Classname -- Its not mandatory, but recommeneded to start the class name with uppercase characters..

# class List:
#     pass

# class First:
#     name = "rajesh"  # attributes.

#     def data(email): # methods
#         return email


# class First:
#     name = "ramesh"  # attributes
#     print(name)

#     def info(self): # methods
#         return "HI {}".format(self.name)


# obj = First()   # object 
# print(obj.name)

# print(obj.info())

# this -- java
# self -- python


# name = "ramesh"
# # print(name)

# def info():
#     return name 

# print(info())

# __init__ -- method: constructor---


class Employee:

    # this method will be called by default when we are calling the class.
    def __init__(self,name,email):
        self.name = name  # self will be taken as Employee
        self.email = email
        pass

    def emp_data(self):
        return "Hi {},your work email is {}".format(self.name,self.email)

    def send_email(self):
        return "Confirmation email is sent to {}".format(self.email)


obj = Employee("ramesh","ramesh@gmail.com")


obj1 = Employee("suresh","suresh@gmail.com")

print(obj.emp_data())

print(obj.send_email())

print(obj1.emp_data())

print(obj1.send_email())