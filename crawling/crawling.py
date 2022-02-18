import pandas as pd
from unittest import result
from selenium import webdriver
from bs4      import BeautifulSoup

from pprint   import pprint
'''
selenium을 이용해 음료 리스트에서 상세페이지 접근 후 음료 상세정보 크롤링
크롤링한 데이터 pandas 이용해 csv 변환
'''
# webdriver로 사이트 접근
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

products = soup.select('.product_list dd a')
result = []

for product in products:
    product = [product.find('img')['alt'],product['prod']]
    driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={product[1]}')

    detail_source = driver.page_source
    detail_soup   = BeautifulSoup(detail_source,'html.parser')
    
    id = '.product_info_content'

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

# 상세정보 dictionary로 저장
    dic     = {}

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
    dic['pro_id']      = product[1]
    result.append(dic)
    pprint(result)

# dict -> csv 변환(pandas이용)
    csv_data = pd.DataFrame(result)
    csv_data.to_csv('prod_drick.csv')