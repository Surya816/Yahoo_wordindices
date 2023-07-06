# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:36:49 2023

@author: bskk8
"""

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def mongodb_client():
    
    """
        Creates MongoDB client
    """
    
    client = MongoClient('mongodb://localhost:27017/')
    return client

def selenium_client():
    
    """
        Creates Selenium driver object to navigate through webpage
    """
    driver = webdriver.Chrome('search-ms:displayname=Search%20Results%20in%20Downloads&crumb=location:C%3A%5CUsers%5Cbskk8%5CDownloads\chromedriver_win32 (1)')
    return driver

def get_symbols(driver, client):
    
    """
        Get Indices from webpage
    """
    
    driver.get('https://finance.yahoo.com/world-indices/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADQYLEjAfIUurhaAVhwg_iwL-NUq6cUoOrQrpaeEEK3tQ7Ma_jo7eAk0oB_gCyMLBPlSAi1HspVQ8nEZe-r2lO_ofJlUrVco2K_cl55W8F59RsuuJi0Ly_n3tt0nPvd8QFwfc6sF1bIDLlY3bDGP15pFHEHgFDoIDH36a8pLaa6M')
    driver.maximize_window()
    new_page = driver.page_source
    soup = BeautifulSoup(new_page)

    symbols_tag = soup.findAll('a', class_="Fw(600) C($linkColor)" )

    symbols_table = []

    for each_symbol in symbols_tag:
        symbol = each_symbol.text.strip()
   
        symbols_dict ={}
            
        symbols_dict["Symbols"] = symbol
        
        symbols_table.append(symbols_dict)
    data = symbols_table
    return data

def get_symbol_links(driver):
    
    """
        Get hyperlinks of individual Indices to get details like summary, chart
        data
    """
    driver.get('https://finance.yahoo.com/world-indices/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADQYLEjAfIUurhaAVhwg_iwL-NUq6cUoOrQrpaeEEK3tQ7Ma_jo7eAk0oB_gCyMLBPlSAi1HspVQ8nEZe-r2lO_ofJlUrVco2K_cl55W8F59RsuuJi0Ly_n3tt0nPvd8QFwfc6sF1bIDLlY3bDGP15pFHEHgFDoIDH36a8pLaa6M')
    driver.maximize_window()
    symbol_links = driver.find_elements(By.CSS_SELECTOR,"[data-test='quoteLink']")
    return symbol_links
    
def insert_symbols(client, data):
    
    """
        Insert Indices to DB
    """
    
    db = client['yahoo1']

    collection = db["symbols_table"]
    collection.insert_many(data)
    print("inserted symbols into db")
    

def get_summary_data(driver, client, symbol_links, update_db):
    
    """
        Clicks hyperlink and reads summary and inserts into DB
    """
    try:
        
        symbol_links.click()
        time.sleep(5)
        
        summary = driver.find_elements(By.CSS_SELECTOR,'[class = "C($primaryColor) W(51%)"]')


       
        summary_table = []
        
        for s in summary:
            summary_table.append(s.text)
            
        
        summary_table_values = []
        
        summary_values = driver.find_elements(By.CSS_SELECTOR,'[class = "Ta(end) Fw(600) Lh(14px)"]')

        for t in summary_values:
            summary_table_values.append(t.text)
        
        summary_dict = {}
        for x,y in zip(summary_table, summary_table_values):
            summary_dict[x] = y
        
        db = client[update_db]
        SUMMARY_COLLECTION = "summary_collection"+str(i+1)
        collection = db[SUMMARY_COLLECTION]
        
        collection.insert_one(summary_dict)
            
        
    except:
        print("closing driver")
        driver.close()
        
    

def get_chart_data(driver, client, previous_date, update_db):
    
    """
        Clicks Chart and takes screenshot and save it to local filesystem and
        then inserts into DB in Binary data
    """
    
    

    time.sleep(5)
    current_date = date.today().strftime("%Y-%m-%d")
    chart = driver.find_element(By.XPATH,'//*[@id="quote-nav"]/ul/li[2]/a')
    chart.click()
    
    time.sleep(3)
    
    try:
        cancel = driver.find_element(By.CSS_SELECTOR,'[class = "H(18px) W(18px) Va(m)! close:h_Fill(white)! close:h_Stk(white)! Cur(p)"]')
        cancel.click()
        time.sleep(2)
        
    except:
            pass
        
    latest_chart = driver.find_element(By.XPATH,'//*[@id="chart-toolbar"]/div[1]/div[2]/div/div/div[1]/span')

    latest_chart.click()

    time.sleep(2)
    from_date = driver.find_elements(By.XPATH,'//*[@id="dropdown-menu"]/div[3]/div[1]/div/div[1]/form/div/label/input')
    to_date = driver.find_elements(By.XPATH,'//*[@id="dropdown-menu"]/div[3]/div[2]/div/div[1]/form/div/label/input')

    from_date[0].clear()
    time.sleep(2)
    from_date[0].send_keys(previous_date)
    
    
    to_date[0].clear()
    time.sleep(2)
    to_date[0].send_keys(current_date)
    


    time.sleep(1)

    
    chart_date_apply = driver.find_element(By.CSS_SELECTOR,'[class = "C(white) Fw(500) Px(15px) Py(9px) Bdrs(3px) Bd(0) Fz(s) D(ib) Whs(nw) Miw(90px) Bgc($linkColor) Bgc($linkActiveColor):h"]')

    chart_date_apply.click()
     


    scroll_offset = 0
    scroll_increment = 300 
    
    for _ in range(2):  
         
         script = f"window.scrollTo(0, {scroll_offset});"
         driver.execute_script(script)
    
         
         scroll_offset += scroll_increment
             
         
    time.sleep(3)
 
    CHARTS_NAME = "chart"+str(i+1)+".png"
    CHART = "chart"+str(i+1)
    
    minichart = driver.find_element(By.CSS_SELECTOR,'[class = "stx-holder stx-panel-chart"]')
    minichart.screenshot(CHARTS_NAME)


    time.sleep(2)
    
    import glob
    
    directory = 'C://Users/bskk8'
    file_pattern =CHARTS_NAME
    file_paths = glob.glob(directory + '//' + file_pattern)
    
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            
            image_data = file.read()
    db = client[update_db]
    collection = db[CHART]
    image_doc = {'image': image_data}
    collection.insert_one(image_doc)
    time.sleep(5)
    
    date1 = {}

    date1["Date"] = current_date



    db = client['yahoo1']

    collection = db["Previous_date"]
    collection.insert_one(date1)

def get_previous_date(client):
    
    """
        To read last inserted date
    """
    
    db1 = client["yahoo1"]
    update_db = ""
    previous_date = ""
    try:
        collection = db1["Previous_date"]
        dtlst = []
        data = collection.find()
        for document in data:
            old_date = (document['Date'])
            dtlst.append(old_date)
    
        previous_date = dtlst[-1]
        update_db = "yahoo2"
        
    except:
        
        current_date = date.today()
        previous_date = current_date - relativedelta(years=1)
        update_db = "yahoo1"
    return previous_date, update_db

def read_symbols_data(driver, client):
    
    """
       Identify if Indices are already inserted, if not we will insert into DB
    """
   
    db1 = client["yahoo1"]
    collection = "symbols_table"
    
    if collection in db1.list_collection_names() :
        print("true")
        return
    else:
        print("in except")
        symbol_data = get_symbols(driver, client)
        insert_symbols(client, symbol_data)
        return 
        
def get_historical_data(driver, client, previous_date,update_db):
    
    """
        Reads Historical data and inserts into DB based on previous run date and current date
    """
    try:
        
        Historical_data = ""
        
        Historical_data = driver.find_element(By.CSS_SELECTOR,'[data-test="HISTORICAL_DATA"]')
        
        Historical_data.click()
        time.sleep(2)

        date_obj = datetime.strptime(previous_date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%m-%d-%Y")
        
        to_date_obj = datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
        to_date = to_date_obj.strftime("%m-%d-%Y")
            
        Historic_date = driver.find_element(By.CSS_SELECTOR,'[class = "C($linkColor) Fz(14px)"]')
        Historic_date.click()
        time.sleep(2)
        
        from_Hist = driver.find_element(By.CSS_SELECTOR,'[name = "startDate"]')
        from_Hist.clear()
        time.sleep(2)
        from_Hist.send_keys(formatted_date)
       
        to_hist = driver.find_element(By.CSS_SELECTOR,'[name = "endDate" ]')
        to_hist.clear()
        
        to_hist.send_keys(to_date)
        
        Done = driver.find_element(By.CSS_SELECTOR,'[class = " Bgc($linkColor) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($linkActiveColor):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)"]')
        Done.click()
        time.sleep(2)
        
        Apply= driver.find_element(By.CSS_SELECTOR,'[class = " Bgc($linkColor) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($linkActiveColor):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)"]')

        Apply.click()
        time.sleep(2)
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

    
        
        rows = Historical_table.find_elements(By.TAG_NAME,'tr')
        
        
    
        Historical_table_data =[]
        Historical_table_data1 =[]
        for row in rows: 
            
            cells = row.find_elements(By.TAG_NAME,'td')
            row_data = [cell.text for cell in cells]
            Historical_table_data.append(row_data)
        
    
        Historical_table_data1 = Historical_table_data[1:]
    
        Historical_table_data1
        HISTORICAL_DATA = []
    
        for j in range (0,len(Historical_table_data1)-1):
            
            my_dict = {}
            
            my_dict["Date"]         = Historical_table_data1[j][0]
            my_dict["Open"]         = Historical_table_data1[j][1]
            my_dict["High"]         = Historical_table_data1[j][2]
            my_dict["Low"]          = Historical_table_data1[j][3]
            my_dict["Close*"]       = Historical_table_data1[j][4]
            my_dict["Adj Close**"]  = Historical_table_data1[j][5]
            my_dict["Volume"]       = Historical_table_data1[j][6]
        
        
            HISTORICAL_DATA.append(my_dict)
            
        
        time.sleep(2)
        
    
        HISTORIC_COLLECTION = "History_collection"+str(i+1)
    
        db = client[update_db]
        
        collection = db[HISTORIC_COLLECTION]
        
        collection.insert_many(HISTORICAL_DATA)
        
        time.sleep(2)
        print("captured historic data")
        
    except:
        
        if Historical_data:
            driver.back()
            time.sleep(2)
            driver.back()
            time.sleep(2)
            driver.back()
            time.sleep(2)
            
            
        else:
        
            driver.back()
            time.sleep(2)
            driver.back()
            
            time.sleep(2)
    
    
    
    time.sleep(3)
    
client = mongodb_client()
driver = selenium_client()
previous_date, update_db = get_previous_date(client)

read_symbols_data(driver,client)

symbol_links = get_symbol_links(driver)

if previous_date != str(date.today()):
    for i in range(0,2):

        get_summary_data(driver, client, symbol_links[i], update_db)
        get_chart_data(driver, client, str(previous_date), update_db)
        get_historical_data(driver, client, str(previous_date), update_db)
        symbol_links = get_symbol_links(driver)
else:
    print("Today's data is already inserted to DB")
    

