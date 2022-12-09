# CSV - Comma Seperated Values...

import csv

# with open('first_cls.csv','r') as file_data:
    # print(file_data)
    # csv_data = csv.reader(file_data)
    # # print(list(csv_data))
    # next(csv_data)
    # for row in csv_data[5:]:
    #     # if row[4] == "Hyderabad":
    #     print(row)
    # csv_data = csv.DictReader(file_data)
    # # printdict(csv_data)
    # for row in csv_data:
    #     print(row,end=",")

    # print(csv_data)

with open("second_cls.csv",'w',newline="") as file_data:
    csv_data = csv.writer(file_data)

    # csv_data.writerow(['Name','Email','Mobile','Company','City']) # single row of data at a time.
    csv_data.writerows([['Suresh', 'Suresh@gmail.com', '8489984887', 'Infosys', 'Bangalore'],['Ramesh', 'Ramesh@gmail.com', '9894894899', 'Wipro', 'Hyderabad']]) # multiple rows of data at a time.
