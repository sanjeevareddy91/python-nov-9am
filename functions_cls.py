# functions : Sets of lines of code which performs a specific task..
    # Main Features of functions is code reusuability..


# a=65
# b=73

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a=12
# b=34

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Syntax for Functions:

# def -- keyword for defining the function.
"""
def function-name():
    statements
"""

# a=43
# b=65

# def arth_ops():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# print("Hello")
# arth_ops()
# print("world")

# a=12
# b=32

# arth_ops()

# print(a)
# print(b)

# Arguments declaration into the function..

# def arth_ops(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# arth_ops(43,65)
# arth_ops(12,32)

# print(a)

# Arguments inside the funtion can be declared in 5 ways..

# 1) Positional Arguments -- assiging the values to the arguments based upon the position..
# 2) Deafult Arguments -- 
# 3) Keyword Arguments
# 4) Arbitrary Positional arguments
# 5) Arbitrary Keyword Arguments 



# 1st Positional Arguments:
# def email_sending(name,email):
#     print("Hi {}, welcome to the Team, we have sent a confiramtion email to {}".format(name,email))

# # email_sending("rajesh","rajesh@gmal.com")

# email_sending(input("enter name:"),input("enter email:"))


# 2) Default arguments : Passing a default value to an argument at the function declaration only..
    # if value to that default is passed at the function call, it will override the default value..
# def emp_info(name,email,location="bangalore"):
#     print("HI {} your email id is {} and your work location is {}".format(name,email,location))


# emp_info("suresh","suresh@digital-lync.com","Hyderabad")

# emp_info("ramesh","ramesh@digital-lync.com")


# While declaring the function all the positional has to declared first then the default has to be declared..

# def emp_info(name,location="bangalore",email):
#     print("HI {} your email id is {} and your work location is {}".format(name,email,location))


# emp_info("suresh","suresh@digital-lync.com","Hyderabad")

# emp_info("ramesh","ramesh@digital-lync.com")



# We have to pass the values tothe function call in the same order that we followed while declaring the function..
# def emp_info(name,location="bangalore",email="suport@digital-lync.com"):
#     print("HI {} your email id is {} and your work location is {}".format(name,email,location))


# emp_info("suresh","suresh@digital-lync.com","Hyderabad")

# emp_info("ramesh","ramesh@digital-lync.com")

# emp_info("mahesh")

# Keyword Arguments: Passing the values to the function call based on the key name..

# def emp_info(name,location="bangalore",email="suport@digital-lync.com"):
#     print("HI {} your email id is {} and your work location is {}".format(name,email,location))


# emp_info(email="suresh@gmail.com",location="Chennai",name="suresh")


# once keyword argument is declared afterthat evertthing should be keyword arguments only..
# emp_info(email="ramesh@digital-lync.com",location="Mumbai","ramesh")



# emp_info("ramesh",name="venkat") # error(multiple values are being assigned for name varibale)

# 4) arbitarary positional arguments: passing multiple positional arguments..

# * 

# def cal_trans(*trans):
#     print(trans)
#     total = 0
#     for ele in trans:
#         total = total+ele
#     print(total)
#     print("Your credit statement for this month is {}".format(total))

# cal_trans(2145.67,435.12,999.0)

# cal_trans(5675.65,3142.54,1000,435.12)

# cal_trans(657.65,3243.64,7583,3244.76,547.54)

# Arbitrary Keyword Arguments:
# **


# def cal_trans(**trans):
#     print(trans)
#     total = 0
#     # trans.pop('name')
#     for ele in trans:
#         if ele == 'name':
#             continue
#         total+=trans[ele]
#     print("Hi {} , Your credit statement for {} months is {}".format(trans.get('name'),len(trans),total))

# cal_trans(jan=43334,feb=6747,name="rajesh",mar=6478)

# cal_trans(mar=4352,jan=64747,name="suresh",sep=56363,apr=5633)

# cal_trans(aug=5338,jan=67272,feb=6262,mar=5629,apr=6373,name="venkat")


# def cal_trans(*trans,**details):
#     print(trans)
#     print(details)
#     total = sum(trans)
#     print("HI {},your credit card statement for this month of amount {} has been sent to you email id {}.".format(details['name'],total,details['email']))

# print(cal_trans(4332,57578,533,name="suresh",email="suresh@gmail.com"))

# cal_trans(4332,57578,name="suresh",email="suresh@gmail.com",533) # error


# return -- Mostly recommended statement will writing the function. 
    # once return is reached after that if you have some statements as well, that will not be executed..


# print -- it is just a statement for displaying the output..

# def add(a,b):
#     # print(a+b)

#     return a+b
#     print("hello")


# def sub(c):
#     # print(add(5,4))
#     return (add(5,4)-c)
#     return (add(10,12)-c)


# print(sub(6))

# def send_email(email):
#     info = sendmail("Hi, we have sent an email to your email id",email)

#     if info.status_code == 200:
#         return {"suceess":True}
#     else:
#         return {"success":False}

# data = send_email("gsanjeevreddy91@gmail.com")

# print(data['success'])

# if data['success']:
#     do the database operation
# else:
#     print("Email sedning id unsuccessful.")
# name1 = "balakrishna" # global varibales

# def name_info(name): # local varibales
#     global name2
#     name2 = name
#     print(name)
#     print(name1)
#     return name

# print(name_info("Chiranjeevi"))

# print(name1)
# print(name2)


# Recursion : A Function calling itself.

# n! = n*(n-1)!
# 6! = 6*5!
#      6*5*4!
#      6*5*4*3!
#      6*5*4*3*2!
#      6*5*4*3*2*1!
#      6*5*4*3*2*1

# expr = ""
# def cal_fact(n):
#     global expr
#     if n==1 or n==0:
#         print(expr+str(n))
#         return 1
#     else:
#         expr = expr + "{}*".format(n)
#         print(expr)
#         return n*cal_fact(n-1)  # 6*5*4*3*2*1

# print(cal_fact(6))

# print(cal_fact(1))

# data = {
#     "ZSAZ":56336,
#     "ZASAF":{
#         "DAFFSS":647337,
#         "GSSHHS":4774744,
#         "GHDHGAA":{
#             "HHHGAHA":4535435,
#             "GHAHAHHA":87378287
#         },
#         "JHHJAH":7367672
#     },
#     "HJHJSHA":{
#         "HGHAAGH":983839398
#     },
#     "GHGHAHA":6362762
# }


# lambda function: A function which doesnot have any name declaration at all..

# lambda -- Its the keyword for declaring lambda functions. 

# lambda arguments:expression

# c = lambda a,b : a+b

# print(c(4,5))

# c = lambda a,b : (a+b)*(a-b)


# print((lambda a,b : (a+b)*(a-b))(4,5))

# print(c(3,2))


# map  -- for performing the expression on every element isnide the sequence..


a=[45,12,64,23,65,17,43]

print(list(map(lambda i:i+5,a))) # [50,17,69]

# filter -- Its used for performing the conditional inside the lambda..


# print(list(filter(lambda i:i%2==0,a)))


# b = []

# for ele in a:
#     if ele %2 == 0:
#         b.append(ele+5)


# print(b)

# print(list(map(lambda i:i+5,filter(lambda i:i%2==0,a))))