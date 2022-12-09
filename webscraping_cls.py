# Scraping from Shine.com

# import requests
# from bs4 import BeautifulSoup

# data = requests.get("https://www.shine.com/job-search/python-jobs?q=python")


# # print(data)
# # print(data.content)


# bs_data = BeautifulSoup(data.content,'html.parser')

# # print(bs_data)


# first_div = bs_data.find('div',class_='ParentClass')

# # print(first_div)
# # all_div = first_div.find_all('div',class_="jobCard_jobCard__jjUmu  white-box-border jobCard ")


# all_div = first_div.find_all('div',class_="jobCard_jobCard__jjUmu white-box-border jobCard")
# # print(all_div)

# for ele in all_div:
#     job_title = ele.find('h2').text
#     organisation = ele.find('div',class_='jobCard_jobCard_cName__mYnow').text
#     location = ele.find('div',class_="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2").text
#     print(job_title,organisation,location)
#     print("\n--------------------------------------------------------\n")


# Scraping from Naukri.com

# import requests

# naukri_data = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_e67807c6-a24b-44f9-a17c-ad9341de8d78_3.Q1PDG4YW86MF&ssid=u29mka61mo0000001670560136154")

# print(naukri_data)