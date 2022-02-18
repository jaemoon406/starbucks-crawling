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

# 음료 크롤링
# driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

# html = driver.page_source
# soup = BeautifulSoup(html,'html.parser')

# drinks = soup.select('.product_list dd a')
# result = []

# for drick in drinks:
#     drick = [drick.find('img')['alt'],drick['prod']]
#     driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={drick[1]}')

#     detail_source = driver.page_source
#     detail_soup   = BeautifulSoup(detail_source,'html.parser')

# # 음료 상세정보 dictionary로 저장
#     dic     = {}

#     dic['name']        = drick[0]
#     dic['kcal']        = detail_soup.select_one('.product_info_content .kcal dd').get_text()
#     dic['sat_FAT']     = detail_soup.select_one('.product_info_content .sat_FAT dd').get_text()
#     dic['protein']     = detail_soup.select_one('.product_info_content .fat dd').get_text()
#     dic['fat']         = detail_soup.select_one('.product_info_content .trans_FAT dd').get_text()
#     dic['trans_FAT']   = detail_soup.select_one('.product_info_content .protein dd').get_text()
#     dic['sodium']      = detail_soup.select_one('.product_info_content .sodium dd').get_text()
#     dic['sugars']      = detail_soup.select_one('.product_info_content .sugars dd').get_text()
#     dic['caffeine']    = detail_soup.select_one('.product_info_content .caffeine dd').get_text()
#     dic['cholesterol'] = detail_soup.select_one('.product_info_content .cholesterol dd').get_text()
#     dic['chabo']       = detail_soup.select_one('.product_info_content .chabo dd').get_text()
#     dic['pro_id']      = drick[1]
#     result.append(dic)
#     pprint(result)

# # dict -> csv 변환(pandas이용)
#     # csv_data = pd.DataFrame(result)
#     # csv_data.to_csv('prod_drick.csv')

import re

# 음식 크롤링
driver.get('https://www.starbucks.co.kr/menu/food_list.do')
html = driver.page_source

food_list_soup = BeautifulSoup(html,'html.parser')
bakerys = food_list_soup.select('.product_list dd a')

result = []
for bakery in bakerys:
    bakery = [bakery.find('img')['alt'],bakery['prod']]
    driver.get(f'https://www.starbucks.co.kr/menu/food_view.do?product_cd={bakery[1]}')
    # driver.get('https://www.starbucks.co.kr/menu/food_view.do?product_cd=9300000003922')
    bakery_source = driver.page_source

    bakery_soup = BeautifulSoup(bakery_source,'html.parser')
    ex = bakery_soup.select_one('.product_info_content')
    # print(ex)
    sort = []
    ex = re.sub('(<([^>]+)>)', '', str(ex))
    ex = re.sub('\([^)]*\)','',str(ex))
    ex = re.sub('[ㄱ-휗]','',str(ex))
    sort.append(ex.replace('\n',''))
    # print(sort)
    dic = {}
    nut = sort[0][1:].split()
    print(nut)
    dic['name']        = bakery[0]
    dic['kcal']        = nut[0]
    dic['fat']         = nut[1]
    dic['sat_FAT']     = nut[2]
    dic['trans_FAT']   = nut[3]
    dic['cholesterol'] = nut[4]
    dic['sodium']      = nut[5]
    dic['sugars']      = nut[6]
    dic['chabo']       = nut[7]
    dic['protein']     = nut[8]
    dic['pro_id']      = bakery[1]
    result.append(dic)
    pprint(result)

# dict -> csv 변환(pandas이용)
    csv_data = pd.DataFrame(result)
    csv_data.to_csv('prod_food.csv')
