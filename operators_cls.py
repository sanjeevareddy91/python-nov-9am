# Operators : Its a symbol which performs the operation between 2 operands.

# 1) Arthimetic (+,-,*,/,%,//,**)
# 2) Relational or Comparsion
# 3) Logical Operators
# 4) Assignment Operators
# 5) Membership
# 6) Identity
# 7) Bitwise Operators

# 14/3              14%3            14//3 

# 3)14(4.6
#   12
# -----
#    20
#    18
# ------
#     2


# 3)14(4
#   12
# ------
#    2


# 3)247(82
#   24
# ------
#    07
#     6
# ------
#     1


# 14//3

# 3)14(4.6
#   12
# -------
#   20
#   18
# --------
#    2


# print(14/3)
# print(14%3)
# print(14//3)
# print(247%3)

# # ** -- Power calculation

# print(3*4)
# print(3**4)

# Comparision or Relational Operators(==,!=,>,<,>=,<=) : Output of relational operators will be Boolean value only(True/False).

# print(15==26)

# print(15!=26)

# print(15<26)

# print(15>26)

# print(15<=26)

# print(15>=26)


# Logical Operators(and, or, not)


# A               B               A and B          A or B            not(A)      not(A and B)    not ((A or B) and (A and B))
# -------------------------------------------------------------------------------------------------------------------------------
# T               F                 F                 T                 F             T                        T 
# F               T                 F                 T                 T             T                        T 
# T               T                 T                 T                 F             F                        F 
# F               F                 F                 F                 T             T                        T 

# username1 = "rajesh@gmail.com"
# password1 = "password"

# mobile = "64773763773"
# username2 = input("ENter username:")
# password2 = input("Enter Password:")
# mobile2 = input("Enter mobile:")

# output = (username2==username1 or mobile2==mobile) and password2==password1

# print(output)

# Assignment Operators(=,+=,-=,*=)


# a=65
# print(a)

# # a=a+5

# a+=5 # a=a+5

# print(a)

# a-=10

# print(a)

# a*=3
# print(a)

# a/=2

# print(a)

# Datatypes of Python:
    # 1) Numbers: Any numerical values.
        # integers : Any numerical without decimal point.(a=657567744)
        # floating : Any numerical value with decimal point.(b=7575.65757)
    # 2) Strings: Sequence of anything which is declared inside ' ' or " " or ''' ''' or """ """
        # Ex : name = "Harish"  password='harish@123'
    # 3) Lists : Sequence of multiple values which are declared inside [ ] which are seperated with comma(,).
        # names = ["rajesh","ramesh",'suresh','subash',545,654.767]
    # 4) Tuples: Sequence of multiple values which are declared inside ( ) which are seperated with comma(,).
        # names = ("rajesh","ramesh",'suresh','subash',545,654.767)
    # 5) Dictionaries : Sequence of key:value pairs declared inside { } which are seperated with comma(,).
        # credentials = {"username":"rajesh@gmail.com","password":"rajesh@123"}
    # 6) Sets : Sequence of values declared inside { } seperated with comma(,) which contains unique elements and are unordered..
        # names2 = {"rajesh","ramesh",'suresh','subash',545,654.767,"rajesh",545}



# Datatypes are segrigated into 2 types depending on the behaviour.
    # Immutable Datatypes : Those values which we cannot make chnages after the declaration.(numbers,strings,tuples).
    # Mutuable Datatypes : Those values which we can make changes after declaration.(Lists,Dictionaries,Sets)


# a="Rajesh"

# print(id(a))

# a="rajesh"

# print(id(a))

# a=[23,24,25,26]

# a=6575744644


# # type -- It will return the type of the value.

# print(type(a))

# a='6575744644'

# print(type(a))

# b = 546373.673377333

# print(type(b))

# name = "Harish"

# password='harish@123'

# print(type(name))

# print(type(password))


# names = ["rajesh","ramesh",'suresh','subash',545,654.767,"rajesh",545]

# names1 = ("rajesh","ramesh",'suresh','subash',545,654.767,"rajesh",545)

# names2 = {"rajesh","ramesh",'suresh','subash',545,654.767,"rajesh",545}

# print(names)
# print(names1)
# print(names2)

# Membership Operators(in, not in) : Its used only for checking whether the element is present in the sequence.

# a="python is a best programming language."


# print("a" in a)

# print("z" in a)

# print("best" in a)

# print("be st" in a)


# print("a b" in a)

# print("best, language" in a)

# a=[54653,74,'data','django','fastapi']

# print(74 in a)

# print('a' in a)


# a=(54653,74,'data','django','fastapi')

# print(74 in a)

# print('a' in a)


# print(74 not in a)


# Identity Operators(is, is not):

# a=65

# print(65 is a)

# print(id(65))
# print(id(a))

# print(65 == a)

# a="rajesh"

# print('rajesh' is a)

# print(id(a))
# print(id("rajesh"))

# print("rajesh" == a)


# a=[1,2,3,4]

# print([1,2,3,4] is a)

# print(id(a))
# print(id([1,2,3,4]))

# print([1,2,3,4] == a)

# print([1,2,3,4] is not a)

# Bitwise Operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Left Shift(<<),Right Shift (>>))

# A         B            A & B     A | B       A ^ B    
# ------------------------------------------------------
# 1         0              0         1           1
# 0         1              0         1           1
# 1         1              1         1           0
# 0         0              0         0           0


a=14
b=63

print(a&b)

print(a|b)

print(a^b)

print(bin(a))
print(bin(b))

print(bin(65))
print(bin(49))
# 2)14(
#     2) 7 - 0
#        2) 3 - 1
#           1 - 1

# 2)63 
#     2) 31 - 1
#         2) 15 - 1
#             2) 7 - 1
#                2) 3 - 1
#                   1 - 1

# 001110 - 14
# 111111 - 63
# -----------
# 001110 -(a&b) 14
# 111111 - (a|b) 63
# 110001 -(a^b)  49

# print(14&65)

# 0001110 - 14
# 1000001 - 65
# -------------
# 0000000 - 0(a&b) - 0
# 1001111 - 

# print(14|65)
# print(int('0b1001111',2))

# print(14<<1)
# print(14>>1)

# 00001110 - 14
# 00011100 - 28

# 00000111 - 1

# print(int('111',2))

# print(int('11100',2))


# 101010 - 2+8+32
# 101011 - 1+2+8+32 = 43

# print(int('101010',2))

# print(~(14))