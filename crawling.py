from pprint import pprint
from selenium import webdriver
from bs4      import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

products = soup.select('.product_list dd a')
# pprint(products)
for product in products:
    # pprint(product)
    # pprint(product['class'])
    pprint([product.find('img')['alt'],product['prod']])
