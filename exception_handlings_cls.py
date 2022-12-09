# # exception: Error
# # Exception Handlings : Handling the error..

# # Predefined Exceptions
# # Userdefined Exceptions

# a=[54,68.73,'python',12,0,54,64.8]


# # for ele in a:
# #     print(1/ele)

# # Hanlding this errors is done using exception handlings..

# # try and except:

# # try:
# #     statements
# # except:
# #     statements

# a=[54,68.73,'python',12,0,54,64.8]

# # for ele in a:
# #     try:
# #         print(1/ele)
# #     except:
# #         print("Error Occured!")


# # for ele in a:
# #     try:
# #         print(1/ele)
# #     except TypeError:
# #         print("TypeError Occured!")
# #     except ZeroDivisionError:
# #         print("ZerodivisionError Occured!")
# #     except:
# #         print("Some Error Occured!")
# #     else:
# #         print("Else Statement")

# # Userdefined Exceptions: Exception that an user can define depending on the requirements..


# class LargeError(Exception):
#     pass

# class SmallError(Exception):
#     pass
#     print("Number entered is smaller, Try with larger value!")

# import random

# input_val = random.randint(0,10)
# print(input_val)
# while True:
#     try:
#         input2 = int(input("Enter input2 value:"))
#         if input2 > input_val:
#             raise LargeError
#         elif input2 < input_val:
#             raise SmallError
#         else:
#             print("Number Guessed Correctly.")
#             break
#     except SmallError:
#         print("Number entered is smaller, Try with larger value!")
#     except LargeError:
#         print("Number entered is larger, try with smaller value!")
#     except ValueError:
#         print("Invalid type of data passed, Try with integer values!")

