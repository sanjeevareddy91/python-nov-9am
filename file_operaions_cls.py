# file operations : 

# 3 modes of file operations:
    # reading(r)
    # writing(w)
    # appending(a)


# a file can be opened in 2 ways..

# 1st Syntax:
    # obejct = open(file-path,mode)

# file_data = open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\first_cls.txt','r')

# print(file_data)

# print(file_data.closed)

# file_data.close() # closing the file which is opened..

# print(file_data.closed)

# 2nd Syntax:   
"""
with open(file-path,mode) as object:
    statement

"""

# with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\first_cls.txt','r') as file_data:
#     print(file_data)

# print(file_data.closed)


# Reading : Its for reading the data from the file..
    # read() -- It will read everything inside the text file..
    # readline() -- It can read only 1 line at a time.
    # readlines() -- It will read all the content in the file but as line by line formatwhich return as a list..

# with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\first_cls.txt','r') as file_data:
#     # print(file_data.read())

#     # print(file_data.readline())
#     # print(file_data.readline())
#     # for ele in file_data.read():
#     #     print(ele)

#     # print(file_data.readlines())
#     for ele in file_data.readlines():
#         print(ele)


# Writing : 
    # write()
    # writelines()


# write can create the file if the file is not present aleady..

# writing features is overwriting the previous content and adding the latest content..
# with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\second_cls.txt','w') as file_data:
    # print(file_data)
    # file_data.write("Python web development is growing rapidly.\nDjango Rest Framework is used for apis creation.")
    # file_data.write("Django Rest Framework is used for apis creation.\n")

    # file_data.writelines(["Fullstack is used for web development\n","Django is the rapid growing framework\n"])


# appending -- Adding the content to the previous existing content..

# with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\third_cls.txt','a') as file_data:
#     # print(file_data)
#     # file_data.write("Django Rest Framework is used for apis creation.\n")
#     file_data.writelines(["Fullstack is used for web development\n","Django is the rapid growing framework\n"])

with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\first_cls.txt','r') as file_data:
    data = file_data.readlines()[0:2]
    print(data)

# print(data)

with open('C:\\Users\\Admin\\Documents\\Python9AM-Oct\\third_cls.txt','a+') as file_data:
    # for ele in data:
    #     file_data.write(ele)
    print(file_data.read())
    file_data.writelines(data)
