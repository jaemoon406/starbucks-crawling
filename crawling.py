# from lib2to3.pgen2 import driver
# from urllib import response
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests

# driver = webdriver.Chrome('./chromedriver')
url = 'https://www.starbucks.co.kr/menu/drink_list.do'

# rep = driver.get(url)
# print(driver.current_url)
# # rep = requests.get(url)
# print(rep)
# crome = url.chrome()

# if rep.status_code == 200:
#     soup = BeautifulSoup(rep.text,'html.parser')
# else:
#     print(rep.status_code)
# print(soup.select_one('body > #wrap > #mstopWrap > #gnb > div > nav > div > ul > li.gnb_nav01 > h2 > a'))
# print(soup.select_one('#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(1) > dl > dd'))
#gnb
# print(soup.select_one('#gnb'))
# print(soup.body.find(id='wrap').find(id='mstopWrap').find['gnb_nav01'])
# html = rep.text
# print(html)
#wrap

#mstopWrap
#wrap

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.implicitly_wait(3)
## url에 접근한다.
driver.get(url)
driver.find_element_by_css_selector('#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(3) > dl > dd')
driver.close()