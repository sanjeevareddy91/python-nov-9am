# # datahiding : Providing the restrictions in accessing the attributes or methods outside of the class.

#     # Public Atrributes or Methods: WHich we can access anywhere without restrictions.
#     # Private Attributes or Methods: Can we accessed only inside the class..


# class Father:
#     _address = "Allagadd,Nandyala,AP"

#     def __init__(self,address):
#         self._address = address

#     def _emp_info(self):
#         return "Hi {}, Welcome to the Team".format(self.emp_name)

# class Child(Father):
#     emp_name = "ramesh"
#     __emp_email = "ramesh@gmail.com" # Private Attributes

#     print(Father._address)
#     def __init__(self,address):
#         self._address = address

#     def emp_info(self):
#         return "Hi {}, Welcome to the Team".format(self.emp_name)

#     def emp_email_info(self):
#         return "HI, Your email id {} is updated in DB".format(self.__emp_email)

#     def __emp_address_info(self): # Private Method
#         return "HI, Your address {} is updated.".format(self._address)


#     def dummy(self):
#         return self.__emp_address_info()


# class Third:
#     def data(self):
#         return(Father._address)

# obj = Child("Bangalore")

# # print(obj.emp_name)
# # print(obj.emp_info())

# # print(obj.emp_email_info())

# # print(obj.__emp_email)

# # print(obj.emp_address_info())

# # print(obj._address)


# # obj1 = Father()

# # print(obj1._address)

# # print(obj.__emp_address_info())

# # print(obj.dummy())

# # print(obj.emp_name)

# # print(obj._address)

# # obj.emp_name = "Suresh"

# # print(obj.emp_name)

# # obj._address = "Hyderabad,Telangana"

# # print(obj._address)

# # obj1 = Third()

# # print(obj1.data())

# # accessing the private attributes or methods:

# print(obj._Child__emp_email)


# print(obj._Child__emp_address_info())


# Password generator..

# import string
# print(string.ascii_lowercase)

import random
lower_case = ""
for ele in range(97,123):
    lower_case += chr(ele)

upper_case = ""

for ele in range(65,91):
    upper_case += chr(ele)

print(upper_case)

digits = ""
for ele in range(48,58):
    digits += chr(ele)

print(digits)
print(lower_case)

special_symbols = "!@$_"

print(special_symbols)

password = ""
list1 = [upper_case,lower_case,special_symbols,digits]
random.shuffle(list1)
for ele in list1:
    password += random.choice(ele)

# password += random.choice(lower_case)
# password += random.choice(digits)
# password += random.choice(special_symbols)

print(len(password))
len_range = random.randint(2,8)
all_values = "".join(list1)
# print(all_values)
print(password)
for ele in range(len_range):
    password += random.choice(all_values)

print(password)
# password = list(password)
# random.shuffle(password)

# print("".join(password))