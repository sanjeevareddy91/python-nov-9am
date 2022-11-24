# # Download the library
# # pymysql -- MYSQL
# # psycopg2 -- Postgres
# # sqlite3 -- SQLITE
# # oracle_cx --  Orcale
# # pymongo -- Mongodb

# import pymysql


# sql_conn = pymysql.connect(user='root',password='',host='localhost',database='emp_info')

# print(sql_conn)

# sql_cur = sql_conn.cursor()  # will create a cursor inside the connection..

# # print(sql_cur.execute("show databases"))

# # print(sql_cur.fetchall()) # Will return all the data it fetch during cursor execution..

# # sql_cur.execute('create database emp_info')

# # sql_cur.execute("show tables")
# # print(sql_cur.fetchall())


# # sql_cur.execute("create table emp_personal_data(emp_name varchar(25),emp_email varchar(25),emp_mobile varchar(10),emp_city varchar(20))")

# # sql_cur.execute("show tables")
# # print(sql_cur.fetchall())


# # print(sql_cur.execute('desc emp_personal_data'))

# # print(sql_cur.fetchall())

# # sql_cur.execute("INSERT INTO emp_personal_data(emp_name,emp_email,emp_mobile,emp_city) VALUES('Venkat','venkat@gmail.com','9474491646','Hyderabad'),('Naresh','naresh@gmail.com','7036367584','Bangalore'),('Subash','subash@gmail.com','8937386594','Chennai'),('Suresh','suresh@gmail.com','8474848243','Mumbai')")

# # print(sql_cur.execute("SELECT * from emp_personal_data"))

# # print(sql_cur.execute("SELECT * from emp_personal_data"))

# # sql_cur.execute("SELECT * from emp_personal_data where emp_name='Suresh'")

# # sql_cur.execute('''
# # SELECT * from emp_personal_data where emp_mobile like '7%' and emp_name like 'R%' and emp_city="Hyderabad"''')
# # print(sql_cur.fetchall())

# # sql_cur.execute('''UPDATE emp_personal_data SET emp_mobile="8663765432" WHERE emp_name="Ramesh"''')

# # sql_cur.execute("DELETE from emp_personal_data WHERE emp_name = 'Naresh'")

# # sql_cur.execute('truncate emp_personal_data')


# # sql_cur.execute("drop table emp_personal_data")

# sql_cur.execute("drop database emp_info")
# sql_conn.commit() # commiting the chnages to the database.
# sql_conn.close() # closing the connection with the database.

