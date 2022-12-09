# ATM Task:

# pin1 = 1234
# pin2 = int(input("Enter the pin:"))

# if pin2 == pin1:
#     acc_type1 = "saving"
#     acc_type2 = input("Enter Account Type:")
#     if acc_type2 == acc_type1:
#         amount = input("Enter the amount to withdraw:")
#         print(amount,"is debited from your account.")
#     else:
#         print("Account Type doesnot match!")
# else:
#     print("Pin doesnot match!")


# # ATM2-Task

# pin1 = 1234
# acc_type1 = "current"

# for ele in range(3):
#     pin2 = int(input("Enter Pin:"))
#     if pin2 == pin1:
#         acc_type1 = "saving"
#         acc_type2 = input("Enter Account Type:")
#         if acc_type2 == acc_type1:
#             amount = input("Enter the amount to withdraw:")
#             print(amount,"is debited from your account.")
#             break
#         else:
#             if ele == 2:
#                 print("Account Block!")
#             else:
#                 print("Account Type doesnot match!Try Again!")
#     else:
#         if ele == 2:
#             print("Account Block!")
#         else:
#             print("Pin doesnot match!Try Again!")


# ATM2-Task

# pin1 = 1234
# acc_type1 = "current"
# balance = 10000
# for ele in range(3):
#     pin2 = int(input("Enter Pin:"))
#     if pin2 == pin1:
#         acc_type1 = "saving"
#         acc_type2 = input("Enter Account Type:")
#         if acc_type2 == acc_type1:
#             amount = int(input("Enter the amount to withdraw:"))
#             print(amount,"is debited from your account.")
#             balance = balance-amount
#             print("Your balance is",balance)
#             break
#         else:
#             if ele == 2:
#                 print("Account Block!")
#             else:
#                 print("Account Type doesnot match!Try Again!")
#     else:
#         if ele == 2:
#             print("Account Block!")
#         else:
#             print("Pin doesnot match!Try Again!")

# ATM 4 - Task

# a = "python is a progamming language"

a=input("Enter your String")

char_check = input("ENter your character:")
which_occ = int(input("Enter which occurence:"))

# print(a.count(char_check))
# print(which_occ)
# if a.count(char_check) >= which_occ:
#     index_count = 0
#     count = 0
#     for ele in a:
#         if ele == char_check:
#             index_count = index_count + 1
#             if index_count == which_occ:
#                 print(char_check,which_occ,"rd occurence","is at",count,"index location")
#                 break
#         count+=1

# else:
#     print(char_check,"has occured only ",a.count(char_check),"times")