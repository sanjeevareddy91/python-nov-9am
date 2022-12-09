# Dictionaries : Sequence of key:value pair which are seperated with comma(,) declared inside { } which contains unique keys..

dict1 = {"name":"rajesh","email":"rajesh@gmail.com","mobile":7847484765,"companies":["TCS","Infosys","Wipro"]}

# print(dict1)

# print(type(dict1))

# dict2 = {"name":"rajesh","email":"rajesh@gmail.com","mobile":7847484765,"companies":["TCS","Infosys","Wipro"],"email":"rajesh123@gmail.com"}

# print(dict2)

# # Dictioary keys should be immutable..

# dict2 = {"name":"rajesh",1:"54","mobile":7847484765,("cities",):["Bangalore","Chennai","Hyderabad"],"companies":["TCS","Infosys","Wipro"],"email":"rajesh123@gmail.com"}

# print(dict2)

# dict2 = {"name":"rajesh",1:54,"mobile":7847484765,["cities",]:["Bangalore","Chennai","Hyderabad"],"companies":["TCS","Infosys","Wipro"],"email":"rajesh123@gmail.com"}

# Dictionary Values can be of any datatype..


dict1 = {"name":"rajesh","email":"rajesh@gmail.com","mobile":7847484765,"companies":["TCS","Infosys","Wipro"]}

# [] for accessing keys inside the dictionary..

# dict-name[key-name]

# print(dict1["email"])

# print(dict1["companies"])

# print(dict1["address"])

# Dictionaries are mutuable..

# dict1["address"] = "#305,Chitrapuri COlony, LIG-6,Manikonda,Hyderabad"

# print(dict1)

# dict1['mobile'] = 64376738837

# print(dict1)

# dict2 = {"name":"rajesh","email":"rajesh@gmail.com","mobile":7847484765,"companies":["TCS","Infosys","Wipro"],"email":"rajesh123@gmail.com"}

# print(dict1+dict2)


# dict1 = {
#     "teams":{
#         "CSK":3,
#         "MI":4,
#         "KKR" : 2,
#         "RR" : 1,
#         "DC" : 1
#     },
#     "captains":{
#         "chennai" : "Dhoni",
#         "mumbai" : "Rohit",
#         "kolkata" : "Gambhir",
#         "rajasthan" : "Warne",
#         "hyderabad" : "Glichrist"
#     }
# }

# print(dict1["captains"]["hyderabad"])

# print(dir(dict))

# update() -- This is for adding a dictionary into other dictionary..

dict1 = {"name":"rajesh","email":"rajesh@gmail.com","mobile":7847484765,"companies":["TCS","Infosys","Wipro"]}

# dict2 = {
#     "email":"rajesh13@gmail.com",
#     "city":"hyderabad",
#     "position":"Software Engineer"
#     }

# dict1.update(dict2)

# print(dict1)

# get() -- Its used for accessing the key:values inside the dictionary..


# print(dict1.get('email'))

# print(dict1['city'])
# print(dict1.get('city'))

# keys() -- It will return all the keys inside the dictionary..

# print(dict1.keys())

# print(list(dict1.keys()))

# values() -- It will return all the values inside the dictionary..

# print(dict1.values())

# Items() -- will return all key:value pairs as tuples inside the list.

# data = list(dict1.items())

# print(data[1][1])

# copy()

# dict2 = dict1

# dict2 = dict1.copy()

# print(dict1)
# print(dict2)

# dict2['city'] = "hyderabad"

# print(dict1)
# print(dict2)


# fromkeys() -- Its for creating a dictionary from list of elements..

a = [1,"name","email","mobile"]

# dict1 = {}
# for ele in a:
#     dict1[ele] = "sample"

# print(dict1)

# print({}.fromkeys(a,"sample"))


# setdefault() -- giving the default key:value to the dictionary..

# dict1 = {}

# dict1.setdefault('city',"bangalore")

# # dict1['city'] = "Bagalore"

# print(dict1)

# dict1.setdefault('city')

# dict1.setdefault('city',"hyderabad")

# print(dict1)


# dict1 = {1:1,2:8,3:27,4:64,5:125,6:216}

dict1 = {}


# dict1[1] = 10

# print(dict1)

# for ele in range(1,7):
#     dict1[ele] = ele**3

# print(dict1)


# 1st Syntax:
    # {expression for ele in sequence}

# print({ele:ele**3 for ele in range(1,7)})


# for ele in range(1,7):
#     if ele%2 == 0:
#         dict1[ele] = ele**2

# print(dict1)


# 2nd Syntax
    # {expression for ele in sequence if condition}

# print({ele:ele**2 for ele in range(1,7) if ele%2==0})



# for ele in range(1,7):
#     if ele%2 == 0:
#         dict1[ele] = ele**2
#     else:
#         dict1[ele] = ele**3

# print(dict1)

# 3rd Syntax:
    # {expression if condition else expession for ele in sequence}

# print({ele:ele**2 if ele%2 ==0 else ele**3 for ele in range(1,7)})


# dict1 = {"suresh":["24-08-1990","09-10-2001"],"ramesh":"12-09-2001"} -- add


# dict1 = {"suresh":"09-10-2001","ramesh":"12-09-2001"}--update

# "enter name"
# "enter dob"

# do you want to continue yes or No:

# enter Name
# enter dob 

# do you want to continue yes or no:yes
# enter name : suresh
    # this user existed do you want to add or update . 
        # 1.update
        # 2.add
        # enter dob:
