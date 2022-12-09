# # regular_expression : It a pattern concept which we apply on strings itself.


# import re

# # print(dir(re))

# # {} -- Its used for count specification.
# # \d -- digitss
# # \w -- alphanumeric values.

# # pattern - 


# # a=r"756 463-7484"


# str1 = "645 884-8484Please contact me at 738 738-6373"


# str2 = "8444 464-474 can be used to contact me."

# pattern  = r'\d{3} \d{3}-\d{4}'

# # match -- match can perform the check only at the starting of the string itself..


# data = re.match(pattern,str1)

# print(data)


# # search -- search can perform the check at any location inside th string..


# # str1 = "Please contact me at 738 738-6373"

# # data = re.search(pattern,str1)

# # print(data)

# str1 = "Please contact me at 738 738-6373 or 748 536-4747"

# data = re.findall(pattern,str1)

# print(data)

