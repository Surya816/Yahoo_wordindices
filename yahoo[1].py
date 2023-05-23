# -*- coding: utf-8 -*-
"""
Created on Fri May 19 06:20:20 2023

@author: bskk8
"""
Summary_data1 = []
Summary_data2 = []
Summary_data3 = []
Summary_data4 = []
Summary_data5 = []
Summary_data6 = []
Summary_data7 = []
Summary_data8 = []
Summary_data9 = []
Summary_data10 = []
Summary_data11 = []
Summary_data12 = []
Summary_data13 = []
Summary_data14 = []
Summary_data15 = []
Summary_data16 = []
Summary_data17 = []
Summary_data18 = []
Summary_data19 = []
Summary_data20 = []
Summary_data21 = []
Summary_data22 = []
Summary_data23 = []
Summary_data24 = []
Summary_data25 = []
Summary_data26 = []
Summary_data27 = []
Summary_data28 = []
Summary_data29 = []
Summary_data30 = []
Summary_data31 = []
Summary_data32 = []
Summary_data33 = []
Summary_data34 = []
Summary_data35 = []
Summary_data36 = []




Historical_data1 = []
Historical_data2 = []
Historical_data3 = []
Historical_data4 = []
Historical_data5 = []
Historical_data6 = []
Historical_data7 = []
Historical_data8 = []
Historical_data9 = []
Historical_data10 = []
Historical_data11 = []
Historical_data12 = []
Historical_data13 = []
Historical_data14 = []
Historical_data15 = []
Historical_data16 = []
Historical_data17 = []
Historical_data18 = []
Historical_data19 = []
Historical_data20 = []
Historical_data21 = []
Historical_data22 = []
Historical_data23 = []
Historical_data24 = []
Historical_data25 = []
Historical_data26 = []
Historical_data27 = []
Historical_data28 = []
Historical_data29 = []
Historical_data30 = []
Historical_data31 = []
Historical_data32 = []
Historical_data33 = []
Historical_data34 = []
Historical_data35 = []
Historical_data36 = []

# chart1 = []
# chart2 = []
# chart3 = []
# chart4 = []
# chart5 = []
# chart6 = []
# chart7 = []
# chart8 = []
# chart9 = []
# chart10 = []
# chart11 = []
# chart12 = []
# chart13 = []
# chart14 = []
# chart15 = []
# chart16 = []
# chart17 = []
# chart18 = []
# chart19 = []
# chart20 = []
# chart21 = []
# chart22 = []
# chart23 = []
# chart24 = []
# chart25 = []
# chart26 = []
# chart27 = []
# chart28 = []
# chart29 = []
# chart30 = []
# chart31 = []
# chart32 = []
# chart33 = []
# chart34 = []
# chart35 = []
# chart36 = []






SUMMARY_DATA        = [Summary_data1,Summary_data2,Summary_data3,Summary_data4,Summary_data5,Summary_data6,Summary_data7,Summary_data8,Summary_data9,Summary_data10,Summary_data11,Summary_data12,Summary_data13,Summary_data14,Summary_data15,Summary_data16,Summary_data17,Summary_data18,Summary_data19,Summary_data20,Summary_data21,Summary_data22,Summary_data23,Summary_data24,Summary_data25,Summary_data26,Summary_data27,Summary_data28,Summary_data29,Summary_data30,Summary_data31,Summary_data32,Summary_data33,Summary_data34,Summary_data35,Summary_data36]
SUMMARY_COLLECTION  = ['Summary_collection1','Summary_collection2','Summary_collection3','Summary_collection4','Summary_collection5','Summary_collection6','Summary_collection7','Summary_collection8','Summary_collection9','Summary_collection10','Summary_collection11','Summary_collection12','Summary_collection13','Summary_collection14','Summary_collection15','Summary_collection16','Summary_collection17','Summary_collection18','Summary_collection19','Summary_collection20','Summary_collection21','Summary_collection22','Summary_collection23','Summary_collection24','Summary_collection25','Summary_collection26','Summary_collection27','Summary_collection28','Summary_collection29','Summary_collection30','Summary_collection31','Summary_collection32','Summary_collection33','Summary_collection34','Summary_collection35','Summary_collection36']
HISTORICAL_DATA     = [Historical_data1,Historical_data2,Historical_data3,Historical_data4,Historical_data5,Historical_data6,Historical_data7,Historical_data8,Historical_data9,Historical_data10,Historical_data11,Historical_data12,Historical_data13,Historical_data14,Historical_data15,Historical_data16,Historical_data17,Historical_data18,Historical_data19,Historical_data20,Historical_data21,Historical_data22,Historical_data23,Historical_data24,Historical_data25,Historical_data26,Historical_data27,Historical_data28,Historical_data29,Historical_data30,Historical_data31,Historical_data32,Historical_data33,Historical_data34,Historical_data35,Historical_data36]
HISTORIC_COLLECTION = ['Historic_collection1','Historic_collection2','Historic_collection3','Historic_collection4','Historic_collection5','Historic_collection6','Historic_collection7','Historic_collection8','Historic_collection9','Historic_collection10','Historic_collection11','Historic_collection12','Historic_collection13','Historic_collection14','Historic_collection15','Historic_collection16','Historic_collection17','Historic_collection18','Historic_collection19','Historic_collection20','Historic_collection21','Historic_collection22','Historic_collection23','Historic_collection24','Historic_collection25','Historic_collection26','Historic_collection27','Historic_collection28','Historic_collection29','Historic_collection30','Historic_collection31','Historic_collection32','Historic_collection33','Historic_collection34','Historic_collection35','Historic_collection36']
CHARTS_NAME         = ['chart1.png','chart2.png','chart3.png','chart4.png','chart5.png','chart6.png','chart7.png','chart8.png','chart9.png','chart10.png','chart11.png','chart12.png','chart13.png','chart14.png','chart15.png','chart16.png','chart17.png','chart18.png','chart19.png','chart20.png','chart21.png','chart22.png','chart23.png','chart24.png','chart25.png','chart26.png','chart27.png','chart28.png','chart29.png','chart30.png','chart31.png','chart32.png','chart33.png','chart34.png','chart35.png','chart36.png']
CHARTS              = ['chart1','chart2','chart3','chart4','chart5','chart6','chart7','chart8','chart9','chart10','chart11','chart12','chart13','chart14','chart15','chart16','chart17','chart18','chart19','chart20','chart21','chart22','chart23','chart24','chart25','chart26','chart27','chart28','chart29','chart30','chart31','chart32','chart33','chart34','chart35','chart36']

import pymongo

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')




from selenium import webdriver



from selenium.webdriver.common.keys import Keys



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EP
import time


import requests
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome('search-ms:displayname=Search%20Results%20in%20Downloads&crumb=location:C%3A%5CUsers%5Cbskk8%5CDownloads\chromedriver_win32 (1)')

driver.get('https://finance.yahoo.com/world-indices/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADQYLEjAfIUurhaAVhwg_iwL-NUq6cUoOrQrpaeEEK3tQ7Ma_jo7eAk0oB_gCyMLBPlSAi1HspVQ8nEZe-r2lO_ofJlUrVco2K_cl55W8F59RsuuJi0Ly_n3tt0nPvd8QFwfc6sF1bIDLlY3bDGP15pFHEHgFDoIDH36a8pLaa6M')



new_page = driver.page_source

soup = BeautifulSoup(new_page)

symbols_tag = soup.findAll('a', class_="Fw(600) C($linkColor)" )

symbols_tag

symbols_table = []

for each_symbol in symbols_tag:
    symbol = each_symbol.text.strip()
    symbols_table.append(symbol)
    

symbols_table

final_symbols_table = []
for i in range(0,len(symbols_table)):
    symbols_dict ={}
    
    symbols_dict["Symbols"] = symbols_table[i]
    
    final_symbols_table.append(symbols_dict)
    
    
    
    
    
data = final_symbols_table

db = client['yahoo']

collection = db["symbols_table"]
collection.insert_many(data)




symbol_links = driver.find_elements(By.CSS_SELECTOR,"[data-test='quoteLink']")

symbol_links

len(symbol_links)


for i in range(len(symbol_links)):
    symbol_links[i].click()
    time.sleep(5)
    


# symbol_link = driver.find_element(By.CSS_SELECTOR,"[data-test='quoteLink']")
# symbol_link.click()


    summary = driver.find_elements(By.CSS_SELECTOR,'[class = "C($primaryColor) W(51%)"]')

    summary_table = []
    for s in summary:
        summary_table.append(s.text)
     
    # summary_table
        
    summary_table_values = []
    
    summary_values = driver.find_elements(By.CSS_SELECTOR,'[class = "Ta(end) Fw(600) Lh(14px)"]')

    for t in summary_values:
        summary_table_values.append(t.text)

# summary_table_values





    for k in range (1):
        
        summary_dict = {}
        
        summary_dict[summary_table[0]] = summary_table_values[0]
        summary_dict[summary_table[1]] = summary_table_values[1]
        summary_dict[summary_table[2]] = summary_table_values[2]
        summary_dict[summary_table[3]] = summary_table_values[3]
        summary_dict[summary_table[4]] = summary_table_values[4]
        summary_dict[summary_table[5]] = summary_table_values[5]
    
    
        SUMMARY_DATA[i].append(summary_dict)
        
    time.sleep(5)


    db = client['yahoo']
    
    collection = db[SUMMARY_COLLECTION[i]]
    
    collection.insert_many(SUMMARY_DATA[i])
    
    time.sleep(5)

    chart = driver.find_element(By.CSS_SELECTOR,'[data-test="CHART"]')
    chart.click()
    
    time.sleep(3)
    
    try:
        cancel = driver.find_element(By.CSS_SELECTOR,'[class = "H(18px) W(18px) Va(m)! close:h_Fill(white)! close:h_Stk(white)! Cur(p)"]')
        cancel.click()
        time.sleep(2)
        
    except:
            pass
        

    
    scroll_offset = 0
    scroll_increment = 300 
    
    for _ in range(2):  
         
         script = f"window.scrollTo(0, {scroll_offset});"
         driver.execute_script(script)
    
         
         scroll_offset += scroll_increment
             
         
    time.sleep(3)
 

    
    minichart = driver.find_element(By.CSS_SELECTOR,'[class = "stx-holder stx-panel-chart"]')
    minichart.screenshot(CHARTS_NAME[i])


    time.sleep(2)
    
    import glob
    
    directory = 'C://Users/bskk8'
    file_pattern =CHARTS_NAME[i]
    file_paths = glob.glob(directory + '//' + file_pattern)
    
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            
            image_data = file.read()
            # print(image_data)

    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['yahoo']
    
    collection = db[CHARTS[i]]
        
    image_doc = {'image': image_data}
    collection.insert_one(image_doc)
    
        
        
    time.sleep(5)
    
    try:
    
        Historical_data = driver.find_element(By.CSS_SELECTOR,'[data-test="HISTORICAL_DATA"]')
        
        Historical_data.click()
    
    
        
        time.sleep(2)
        Historical_table = driver.find_element(By.CSS_SELECTOR,'[class= "W(100%) M(0)"]')
        
        scroll_offset = 0
        scroll_increment = 5000 
        
        for _ in range(5):  # Adjust the number of times to scroll as needed
              # Execute JavaScript to scroll the page
              script = f"window.scrollTo(0, {scroll_offset});"
              driver.execute_script(script)
        
              # Increment the scroll offset for the next scroll action
              scroll_offset += scroll_increment
         
     
        time.sleep(5)
    # Historical_table_header =[]
    
        
        rows = Historical_table.find_elements(By.TAG_NAME,'tr')
        
        # headers = Historical_table.find_elements(By.TAG_NAME,'tr')
        # header_data =headers[0]
        # Historical_table_header.append(header_data.text)
        
        # Historical_table_header
    
        Historical_table_data =[]
        Historical_table_data1 =[]
        for row in rows: 
            
            cells = row.find_elements(By.TAG_NAME,'td')
            row_data = [cell.text for cell in cells]
            Historical_table_data.append(row_data)
        
    
        Historical_table_data1 = Historical_table_data[1:]
    
        Historical_table_data1[i]
        len(Historical_table_data1)
        
    
    
        HISTORICAL_DATA[i] = []
    
        for j in range (0,len(Historical_table_data1)-1):
            
            my_dict = {}
            
            my_dict["Date"]         = Historical_table_data1[j][0]
            my_dict["Open"]         = Historical_table_data1[j][1]
            my_dict["High"]         = Historical_table_data1[j][2]
            my_dict["Low"]          = Historical_table_data1[j][3]
            my_dict["Close*"]       = Historical_table_data1[j][4]
            my_dict["Adj Close**"]  = Historical_table_data1[j][5]
            my_dict["Volume"]       = Historical_table_data1[j][6]
        
        
            HISTORICAL_DATA[i].append(my_dict)
            
            HISTORICAL_DATA[i]
        
        
        
    
    
    
        db = client['yahoo']
        
        collection = db[HISTORIC_COLLECTION[i]]
        
        collection.insert_many(HISTORICAL_DATA[i])
        
        time.sleep(2)
        
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        
    except:
        
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    
    
    
    time.sleep(3)
    
    symbol_links = driver.find_elements(By.CSS_SELECTOR,"[data-test='quoteLink']")
    time.sleep(3)
    
    
    
    
   
