# # mutlithreading : 

# # Thread : Light Weighted Process..

# import time
# import threading
# def square(a):
#     for ele in a:
#         time.sleep(0.5)
#         print(ele**2)


# def cube(a):
#     for ele in a:
#         time.sleep(0.2)
#         print(ele**3)


# a=[2,3,4,5]

# t = time.time()
# # square(a)
# # cube(a)

# t1 = threading.Thread(target=square,args=(a,))

# t2 = threading.Thread(target=cube,args=(a,))

# t1.start()

# t2.start()

# t1.join()
# t2.join()

# print("Time Taken",time.time() - t)


# # print(hex(43))