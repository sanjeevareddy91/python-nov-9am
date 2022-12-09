# Sets - Sequence of elements which are declared inside { } seperated with comma(,) which contains unique elements and which are unordered.

set1={32,"python",54,5.9,"django",32,5.9}

print(set1)


# Sets can contains only immutable datatypes..


# set2 = {32,45,'data',[2,3,4]} -- error(sets cannot contain mutuable elements.)

# Sets are mutubale..

# Set MEthods : add,update, pop,remove,discard,clear,copy

# print(dir(set))

# add -- its for adding a sinlge element into the set..

# set1.add(78)

# print(set1)

# # update() -- its for adding multiple elements into the set at a time..

# set1.update([21,22,23])

# print(set1)

# set1.update(["datascience","devops"])

# print(set1)

# remove() -- Its for removing the elementfrom the sequence.
# set1.remove('devops')

# print(set1)

# discard() -- Its for removing the elementfrom the set.

# set1.discard('devops')

# print(set1)

# set1.remove(101)

# print(set1.discard(101))

# print(set1.pop())

# clear() -- remove all the elements and make it as empty..

# set1.clear()

# print(set1)

# print(set1)

# copy() -- 

# a={43,65,'python',21.65,86}

# # b = a 

# b = a.copy()

# print(b)
# print(a)

# b.add(78)

# print(b)
# print(a)

# Sets Operations
    # union(|) -- Adding the element of both the sets and making it as single set..
    # intersection(&) -- common elements between both the sets..
    # difference(-) Removing the second set element which are present in first set and return only the remaining element from the first element..
    # symmetric_difference() -- uncommon elements of both the sets..


a={43,65,'python',21,21.65,86}
b={21,'django',63,65,39}

# print(a.union(b))

# print(a|b)

# print(a.intersection(b))
# print(b.intersection(a))

# print(a&b)

# 64-54

# 54-64

# print(a.difference(b))  # {43,65,'python',21,21.65,86} - {21,'django',63,65,39} = {43,'python',21.65,86}

# print(b.difference(a)) # {21,'django',63,65,39} - {43,65,'python',21,21.65,86} = {'django',63,39}

print(a-b)
# print(b-a)

# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))

print(a^b)


print(a)
print(b)

# a = a.difference(b)

# a.difference_update(b)

# print(a)
# print(b)

# a.symmetric_difference_update(b)

# print(a)
# print(b)

# a.intersection_update(b)

# print(a)
# print(b)

# a+b 


# issuperset
# issubset
# isdisjoint()

# a={43,65,'datascience',12,68,79}

# b = {79,12,43}

# print(a.issuperset(b))

# print(b.issubset(a))

# print(a.issubset(b))

# # isdisjoint() - no common element between both the sets..

# print(a.isdisjoint(b))


