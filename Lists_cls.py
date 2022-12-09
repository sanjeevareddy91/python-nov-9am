# Lists - Sequence of multiple values seperated with comma(,) which are declared inside [ ].

list1 = [43,56.87,'python',46,567.758,'django']

list2 = [43,56.87,'python',46,567.758,'django',[11,12,13]] #-- nested list

# Accessing the elements inside the list can be done using --- indexing.

# indexing will start from 0.
# [] are used for accessing the indexing..

# print(list1[4])
# print(list1[2])


# print(list1[1:5])

# print(list1[0:6:2]) # slicing

# Negative indexing -- which will start from -1..

# print(list1[-2])

# Nested Indexing -- performing the indexing on other indexing outputs..
# list2 = [43,56.87,'python',46,567.758,'django',[11,12,13]]

# print(list2[6][2])

# # print(list2[5][4])

# # print(list2[0])

# print(list1[2][1])

# print(list1[2][-1])

# Basic Operations 
    # Concatenation : Adding of 2 list element into a single list..
    # Repetition : Repeating the elements in the list multiple no.of time.

# print([1,2,3,4]+[11,12,13])

# print([1,2,3,4]*3)

# Lists are Mutuable.

# list2 = [43,56.87,'python',46,567.758,'django',[11,12,13]]

# print(list2)
# list2[0] = 29

# print(list2)

# del list2[4]

# print(list2)

# Lists MEthods:

# print(dir(list)) #-- will give all the methods we can perfomr on list.


# Adding Methods:
    # append,extend,insert
# Removal Methods:
    # remove ,pop,clear
# Accessing Method:
    # Index,Count

list2 = [43,56.87,'python',46,567.758,'django',[11,12,13]]

# append() -- Its used for adding an element into the list..

# print(list2)
# list2.append(65)

# print(list2)

# list2.append("Datascience")

# print(list2)

# list2.append(["hyderabad","Bangalore","Mumbai"])

# print(list2)

# Extend -- Its used for adding the elements into the list at last index.

# list2.extend("Datascience")

# print(list2)

citis = ['hyderabad', 'Bangalore', 'Mumbai']
list2 = [43, 56.87, 'python', 46, 567.758, 'django', [11, 12, 13], 65, 'Datascience']

# for ele in citis:
#     list2.append(ele)

# list2.extend(citis)

# list2.append(citis[0])
# print(list2)

# insert() -- Its for adding the single element at the specific index value..

list2.insert(4,"Datascience")

# print(list2)

# remove() -- It will remove the specified element from the List.
# 
# list2.remove(567.758)

# print(list2)

# del list2[3]

# print(list2)

# list2.remove(list2[3])

# print(list2)


# # pop() - It will remove he last element from the list..

# list2.pop()

# print(list2)
# 
# list2.clear()

# print(list2)

# index() -- It will return the index value of a element..

# print(list2.index(46))

# count() -- How many times a particular element is repeated inside the list..

# print(list2.count(46))

# sort() -- Its for sorting the elements in the list by default ascending.

list2 = ["Hyderabad","Mumbai","Bangalore","Chennai","Delhi","Nagpur"]

# list2.sort()

# list2.reverse()
# list2.sort(reverse=True) # will do sorting in Descending order.

# print(list2)

# reverse() - It will reverse the elements inside the list 

# list2.reverse()

# print(list2)

# list2 = [64,72,32,6452,4,526,31,8793,42,65]

# list2.sort()
# print(list2)

# copy() -- 

a=[23,45,16,18,14]

# b=a 

# b=a.copy()

# print(id(a))
# print(id(b))
# # b=a.copy()

# print(a)
# print(b)

# b.append(78)

# print(a)

# print(b)

a=[43,56.7,"Python","Django",12,[11,12,13]]

# for ele in a:
#     print(ele)

# number_list = []
# other_list = []
# p_list = []
# for ele in a:
#     if type(ele) == int or type(ele) == float:
#         # print(ele)
#         number_list.append(ele)
#     else:
#         if type(ele) == str and ele.startswith('P'):
#             p_list.append(ele)
#         else:
#             other_list.append(ele)
# print(number_list)
# print(other_list)
# print(p_list)


# List Comprehension:

a=[45,62,89,12,64,86,37]

b=[]

# for ele in a:
#     b.append(ele+5)

# print(b)

# # 1st Syntax:
#     # [expression for ele in sequence]

# c = [ele+5 for ele in a]
# print(c)

# for ele in a:
#     if ele%2 == 0:
#         b.append(ele)

# print(b)

# 2nd Syntax:
    # [expression for ele in sequence if condition]

# c = [ele for ele in a if ele%2 == 0]
# print(c)

# a=[45,62,89,12,64,86,37]

# for ele in a:
#     if ele%2 == 0:
#         b.append(ele)
#     else:
#         b.append(ele+1)

# print(b)

# # 3rd Syntax:
#     # [ expression if condition else expression for ele in sequence]
# c = [ele if ele%2==0 else ele+1 for ele in a]

# print(c)

# a=[54,23,65,12,67,15,42,59,36,40]
# Output : - [54,12,42,36,40,23,65,67,15,59]


# a=[32,54,67,(11,12,13)]

# print(a)
# a[3][1] = 21