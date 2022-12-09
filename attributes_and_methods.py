# # Attributes: Varibales defined inside the class is called as attributes..
#     # Instance attributes -- Those attributes which are defined inside the __init__ method and can be access only with object..
#     # Class Attributes -- Those attributes which we can acces using both class and object name..

# # class Employee:
# #     emp_name = "Suresh" # class Attributes
# #     emp_email = "Suresh@gmail.com"

# #     def __init__(self,emp_name,emp_email): # Instance Attributes..
# #         self.emp_name = emp_name
# #         pass


# # obj = Employee("Ramesh","Ramesh@gmail.com")

# # print(obj.emp_name)

# # print(Employee.emp_name)


# # Methods: Functions defined isnide the class are called as methods..
#     # Instance Methods: Those methods which contains self as default argument and can be accessed only with object-name..
#     # Class Methods:
#     # Static Methods:


# class Employee:
#     emp_name = "Suresh" # class Attributes
#     emp_email = "Suresh@gmail.com"

#     def __init__(self,emp_name,emp_email): # Instance Attributes..
#         self.emp_name = emp_name
#         pass

#     # def __init__(self): # Instance Attributes..
#     #     self.emp_name = "Subash"
#     #     pass
    
#     def add_mobile(self,mobile): # instance method
#         self.mobile = mobile
#         return "Hi {}, your mobile number {} is added to the DB.".format(self.emp_name,mobile)

#     def send_otp(self):
#         return "HI {},OTP sent to your mobile number {}".format(self.emp_name,self.mobile)

#     @classmethod
#     def add_mobile_cls(cls,mobile):
#         cls.mobile = mobile
#         return "{} assigned to {} in the DB.".format(mobile,cls.emp_name)

#     @classmethod
#     def send_otp_cls(cls):
#         return "OTP is sent to {},please check {}".format(cls.mobile,cls.emp_name)

#     @staticmethod
#     def add_mobile_static(emp_name,mobile):
#         return "{} assigned to {} in the DB.".format(mobile,emp_name)


#     @staticmethod
#     def send_otp_static():
#         return "OTP is sent to {},please check {}".format(mobile,emp_name)

# obj = Employee("Ramesh","Ramesh@gmail.com")

# # print(obj.add_mobile("9449484998"))

# # print(Employee.add_mobile("489494849485"))

# # obj.emp_name = "Venkat"

# # print(obj.emp_name)

# # print(obj.add_mobile("48449048303"))

# # print(obj.send_otp())

# # print(obj.add_mobile_cls("8393839393"))

# # print(obj.send_otp_cls())

# # print(Employee.add_mobile_cls("839338339"))

# # print(Employee.send_otp_cls())


# print(obj.add_mobile_static("Mahesh","984494894"))