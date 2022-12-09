# Tuples: Sequence of elements seperated with comma(,) declared inside ( ).

# a=(3,6,7.8,'python','django')

# print(a)

# a=(3,) # single value tuple declaration.

# print(a)

# print(type(a))

# b=3,6,7.8,'python','django'

# # () is not mandatory while declaring the tuple, But its mostly recommended..

# print(b)
# print(type(b))

# a=3,

# print(a)

# Accessing the element inside the tuple -- Indexing.

# Index starts from 0..
# [] is used for indexing.

a=(43,76,'datascience',12,56.7,'python')

print(a[3])


# print(a[1:5])

# print(a[0:6:2])

# print(a[-1])

# print(a[5:0:-1])

# # Tuples are immutable.

# # a[1] = 65

# # del a[1]

# a=(32,54,67,[11,12,13])

# a[3][1] = 21

# print(a)

# Basic Operations:
    # Concatenation(+) : Adding 2 tuples and making it as single tuple.
    # Repetition(*) : Repeating the sme elementinside the tuple.

# print((3,4,5)+(13,14,15))

# print((3,4,5)*3)

# print(dir(tuple))

# count() - how many times a particular element is repeated isnide the tuple.

# a=(43,76,'datascience',12,56.7,43,76,43,'python')

# print(a.count(43))

# print(a.index(76))

