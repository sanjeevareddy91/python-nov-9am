# Strings: Anything writtened in between ' ' or " " or """ """..

# sample_str = "Python is a programming language"

# print(sample_str)
# print(type(sample_str))

# sample_str = 'Python is a programming language'

# print(sample_str)
# print(type(sample_str))

# poem = "Twinkle Twinkle Little Star
# How i wonder what you are"


# Mutliline strings- Writing the string in multiple lines between triple quotations.

# poem = """Twinkle Twinkle Little Star
# How I wonder what you are"""

# print(poem)

# # poem = "Twinkle Twinkle" Little Star"

# poem = 'Twinkle Twinkle" Little Star'
# print(poem)


# poem = "Twinkle Twinkle' Little Star"
# print(poem)

# sample_str = "Python is a programming language"

# Accessing the substring inside the string.. -- Indexing..

# Indexing is done using the index value and [].

# Indexing will start from 0..


# print(sample_str[0])

# print(sample_str[10])

# print(sample_str[40]) # error because the index we gave is greaterthan the length.

# len - will return the length of the string.

# print(len(sample_str))

# print(sample_str[31])


sample_str = "Python is a programming language"

# print(sample_str[2:15])

# print(sample_str[4:19])

# Slicing -- performing the jumps on strings.

# print(sample_str[0:23:3])

# Negative Indexing : Performing the indexing in reverse order..

# Negative Indexing will start from -1.

# print(sample_str[-1])

# print(sample_str[-10])


sample_str = "Python is a programming language"

# print(sample_str[-2:-11:1])

# If you want to perform the string in reverse order 3rd argument is mandatory which is a negative value..

# print(sample_str[-2:-11:-1])

# print(sample_str[-2::-1])

# print(sample_str[::-1])  # reversing the string..
# print(sample_str[::-2])

# Basic Operation:
    # Concatenation(+) : Adding of 2 strings and making it as single string.
    # Repitition(*) : Repeating the same string multiple no.of times..

a="Python"
b="Django"

# print(a+b)

# print(a*3)

# print(a+" "+b)

# print((a+" ")*3)

# dir - will give the list of methods that we can perform on value..

# print(dir(str))

# Strings Methods:
    # startswith,endswith,isalpha,isalnum,isdigit,count,capitalize,find,format,index,islower,isupper,lower,upper,join,strip,replace,split,swapcase,title,zfill

# Strings are Immutables -- Once you declare the value we cannot make chnages inside the value..

# a="Python programming in growing in IT"

# # print(a[0])

# a[0] = "p"

# a="python programming in growing in IT"

# print(a)

a="python programming in growing in IT"

# startswith() -- It is used to just check whether the string is starting with what i have specified or not.


b = "P"

# print(a.startswith(b))

# b = "python p"
# print(a.startswith(b))

# b = "pythonp"
# print(a.startswith(b))


# print(a.startswith("python "))

# endswith() -- It is used to just check whether the string is ending with what i have specified or not.

a="python programming in growing in IT"

# print(a.endswith("IT"))

# print(a.endswith(" IT "))

# islower() -- Its for checking whether all the alphabets inside the string are lowercase only..

# print(a.islower())

# a="python programming in growing in it"

# print(a.islower())


# isupper() -- Its for checking whether all the alphabets inside the string are uppercase only..

# print(a.isupper())

# a="PYTHON PROGRAMMING"
# print(a.isupper())


# lower() -- It will convert all the alphabets into lowercase..

a="python programming in growing in IT"

# print(id(a.lower()))


# upper() -- It will convert all the alphabets into uppercase..

a="python programming in growing in IT"

# print(id(a.upper()))

# print(id(a))

# isalpha() - Used to check whether everything insidethe string is alphabets only..

a = "PythonProgramming"

# print(a.isalpha())

# isalnum() - Used to check whwther everything isnide the string is alphabets and numbers only...

a="Python123"

# print(a.isalnum())

# a="123"

# print(a.isalnum())

# a="Python"

# print(a.isalnum())


# isdigit() -- Used to check whether everything isnide the string is numbers only...

# mobile = "79282929898982"

# print(mobile.isdigit())

# mobile = "7928292 9898982"

# print(mobile.isdigit())

# count,capitalize,find,format,index,join,strip,replace,split,swapcase,title,zfill

# count() -- It will return the no.of time a substring is repeatd inside the main string..

a="Python is programming language,Python is used for apis creation"


# print(a.count('a'))

# print(a.count("Python"))

# index -- It will return the index of the element(substring) inside the main string..
    # if element(substring) is repeated multiple times, it will give thefrst occurence index vlue only..

# print(a.index('p'))

# print(a.index('a'))

# print(a.index("Python"))

# # find() -- It will return the index of the element(substring) inside the main string..

# print(a.find('p'))

# print(a.find('a'))

# print(a.find("Python"))


# print(a.index('z'))

# print(a.find('z'))

# difference between find and index is index will give an error when element is not present, but find will return it as -1..


a="Python is programming language,Python is used for apis creation"

# rfind() - Same concept of fidning the index value but from back to front(right to left).

# print(len(a))

# print(a.rfind('p'))

# print(a.rfind('a'))

# print(a.rfind('Python'))

# split() - Its used for spliting the single string into multiple substring based on the characters we specific or by defaultly with " "(space) which will return the output as list..

split_val = a.split() # It will divide the string into multiple string based on space.

# print(a.split('a'))

# \n - newline
# \t - tabspace.

# strip() -- It will remove the escape sequences at the staring and ending of te string.

dummy_str = "\n\tPython is used for \n backend programming in \t developing apis\n"

# print(dummy_str)

# print(dummy_str.strip())

# print(dummy_str.lstrip())

# print(dummy_str.rstrip())

# title,captialize,swapcase

a="Python is Programming languaGE"

# title() - Convert each word starting character into uppercase and remaning into lowercase..

# print(a.title())

# Capitalize() - Convert only starting character of string into uppercase and remaning into lowercase..

# print(a.capitalize())

# swapcase() - will convert lower into upper and upper into lowercase.

# print(a.swapcase())

# join() -- 
# print(split_val)

# a="Pyhton"

# print("@".join(a))

# print("".join(split_val))


# zfill() -- Filling up with 0's..

# a="477878282"

# print(a.zfill(12))

# replace() - Its used for replacing a substring with other string insdie the main string..

# a="Python programming"

# print(a.replace('g','z'))

# dialogue = "Dont trouble the trouble if you trouble the trouble the trouble troubles you i am not the trouble i am the truth Jai ballayya."

# print(dialogue.replace('trouble','problem'))

# print(dialogue.replace('trouble','problem',3))

# .format() 

# {} - for the declaration..

msg = "Hi Sanjeeva, an amount of 500 is being debited from ICICI ATM Gachibowli from your account id 7378227827."


# name = "Suresh"
# amount = "1000"
# bank_name = "HDFC ATM"
# branch_name = "Panjagutta"
# account_id = "38273278278287"

name = input("Enter name:")
amount = input("Enter amoutn:")
bank_name = input("Enter bank name:")
branch_name = input("Enter branh name:")
account_id = input("Enter account id:")

# print("Hi {}, an amount of {} is being debited from {} {} from your account id {}".format(name,amount,bank_name,branch_name,account_id))


# order of declaring the varibales or elements inside the .format is also very important.

# print("Hi {name}, an amount of {amount} is being debited from {bank_name} {branch_name} from your account id {account_id}".format(branch_name=branch_name,account_id=account_id,name=name,amount=amount,bank_name=bank_name))

# f''

# print(f'Hi {name}, an amount of {amount} is being debited from {bank_name} {branch_name} from your account id {account_id}')