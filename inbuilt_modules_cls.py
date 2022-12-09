# # print(help('modules'))

# # math
# # random
# # datetime
# # calendar
# # urllib

# # import math

# # # print(dir(math))

# # print(math.sqrt(25))

# # print(math.pow(3,4))

# # print(math.pi)

# # print(math.e)

# # print(math.exp(4))

# # random()

# # import random

# # print(random.random())

# # print(random.randint(100,999))

# # print(random.randrange(100000,999999))
# # import random

# # a= ["SWIGGYIT",50,"WELCOMEBACK","SWIGGYBIRTHDAY"]

# # print(random.choice(a))

# # print(random.choices(a,k=2))

# # a= ("SWIGGYIT","SWIGGY40","WELCOMEBACK","SWIGGYBIRTHDAY")

# # print(random.choices(a))

# # a= "Python"

# # print(random.choice(a))


# # a = {"name":"ramesh","email":"ramesh@gmail.com","mobile":7474884444}

# # print(random.choice(a))

# # sample()

# # print(random.sample(a,2))


# # print(help(random))


# # datetime module..

# import datetime

# # print(dir(datetime))

# # print(datetime.date())

# # print(dir(datetime.datetime.now()))


# today_date = datetime.datetime.now()
# # print(datetime.datetime.now().date())

# # print(datetime.datetime.today())

# # print(today_date.date())

# # print(today_date.time())

# # print(today_date.date().year)

# # print(today_date.time().hour)

# after_30days = today_date.date() + datetime.timedelta(days=30)

# # print(after_30days)

# # print(type(after_30days))


# # after_10minutes = today_date.time() + datetime.timedelta(minutes=10)

# # # print(after_10minutes)

# # print(type(today_date.time()))

# # print(type(datetime.timedelta(minutes=10)))

# # strptime() -- Its for converting the string date format into python datetime format..

# today_date = "2022-11-20 09:43"

# # print(type(today_date))

# # converted_date = datetime.datetime.strptime(today_date,'%Y-%m-%d %H:%M')

# # print(converted_date)

# # print(type(converted_date))


# # today_date = "12 Nov 2022 09:43 AM"

# # converted_date = datetime.datetime.strptime(today_date,'%d %b %Y %H:%M %p')

# # print(converted_date)

# # strftime() -- converting the python object into string..

# # now_date = datetime.datetime.now()

# # print(now_date)

# # print(type(now_date))

# # str_con_date = now_date.strftime('%Y-%m-%d %I:%M %p')

# # print(str_con_date)

# # print(type(str_con_date))

# # calendar:

# # import calendar

# # print(dir(calendar))

# # print(calendar.isleap(1999))

# # print(calendar.leapdays(2000,2021))

# # print(help(calendar.leapdays))

# # print(list(calendar.day_name))

# # print(calendar.day_abbr[0])

# # print(list(calendar.month_name))

# # print(calendar.monthcalendar(2022,11))

# # print(calendar.month(2022,11))

# # print(calendar.calendar(2022))

# # import urllib.request

# # requests

# # data = urllib.request.urlopen('https://www.programiz.com/python-programming/datetime/strp')


# # print(data.code)
# # print(data.read())

# # External Modules

# # pip  -- python package manager.

# # pip install package-name
# # pip install psycopg2
# # pip install pymysql

# # pip install Instagramy

# # pip uninstall Instagramy -- uninstall the library..

# # pip list or pip freeze -- list of packages you have installed externally..

# from instagramy import InstagramUser

# username = input("Enter your username:")

# user_data = InstagramUser(username)

# print(user_data)

# print(user_data.number_of_followers)

# print(user_data.number_of_followings)

# print(user_data.number_of_posts)

# print(user_data.posts_display_urls)

# # print(dir(user_data))



# virtualenvironments : 

# pip install virtualenv  

# virtualenv environment-name

# cd environment-name\Scripts
# activate -- this will activate the virtualenv..


# install the libraries which you require..
# 
# deactivate -- for deactivating the virtualenv.. 