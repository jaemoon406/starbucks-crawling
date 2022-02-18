from unittest import result
from selenium import webdriver
from bs4      import BeautifulSoup
import pandas

from pprint   import pprint

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

products = soup.select('.product_list dd a')
# pprint(products)

for product in products:
    product = [product.find('img')['alt'],product['prod']]
    driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={product[1]}')

    detail_source = driver.page_source
    detail_soup   = BeautifulSoup(detail_source,'html.parser')
    # pprint(detail_soup.select_one(.product_info_))
    # pprint(detail_soup.select_one('.product_info_content .kcal dd').get_text())
    id = '.product_info_content'
    # print(detail_soup.select_one(f'{id} .kcal dd').get_text)

    kcal        = detail_soup.select_one(f'{id} .kcal dd').get_text()
    sat_FAT     = detail_soup.select_one(f'{id} .sat_FAT dd').get_text()
    protein     = detail_soup.select_one(f'{id} .protein dd').get_text()
    fat         = detail_soup.select_one(f'{id} .fat dd').get_text()
    trans_FAT   = detail_soup.select_one(f'{id} .trans_FAT dd').get_text()
    protein     = detail_soup.select_one(f'{id} .protein dd').get_text()
    sodium      = detail_soup.select_one(f'{id} .sodium dd').get_text()
    sugars      = detail_soup.select_one(f'{id} .sugars dd').get_text()
    caffeine    = detail_soup.select_one(f'{id} .caffeine dd').get_text()
    cholesterol = detail_soup.select_one(f'{id} .cholesterol dd').get_text()
    chabo       = detail_soup.select_one(f'{id} .chabo dd').get_text()
    
    dic     = {}
    result = []

    dic['name']        = product[0]
    dic['kcal']        = kcal
    dic['sat_FAT']     = sat_FAT
    dic['protein']     = protein
    dic['fat']         = fat
    dic['trans_FAT']   = trans_FAT
    dic['protein']     = protein
    dic['sodium']      = sodium
    dic['sugars']      = sugars
    dic['caffeine']    = caffeine
    dic['cholesterol'] = cholesterol
    dic['chabo']       = chabo
    
    result.append(dic)
    pprint(result)

