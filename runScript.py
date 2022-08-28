# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:34:41 2022

@author: Michael
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:08:55 2021

@author: Michael
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

from selenium.common.exceptions import NoSuchElementException


from webdriver_manager.chrome import ChromeDriverManager





stock_list = ["INTC", "MSFT", "CSCO", "AAPL", "AMZN", "GOOG", "JNPR", "VZ", "T", "TMUS"]
booklist = ["The Gruffalo", "The Frog Princess", "Moonlight on the Magic Flute"
            , "Charlotte's Web"]
# booklist = ["Big Easter Adventure"]
dic = {}
# for stock in stock_list:  
#     driver = webdriver.Chrome()
#     driver.get("https://finance.yahoo.com/")
#     search = driver.find_element_by_name("s")
#     search.send_keys(stock)
#     search.send_keys(Keys.RETURN)
#     time.sleep(2)
    
#     histdata = driver.find_element_by_link_text("Historical Data")
#     histdata.click()
#     time.sleep(1)
    
#     download = driver.find_element_by_link_text("Download")
#     download.click()
#     time.sleep(2)
#     driver.close()
    
for book in booklist:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome()
    AR = "NA"
    Lex = "NA"
    
    #AR part
    driver.get("https://www.arbookfind.com/advanced.aspx")
    driver.find_element_by_xpath("//input[@id='radStudent']").click()
    driver.find_element_by_xpath("//input[@id='btnSubmitUserType']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtTitle']").send_keys(book)
    driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_btnDoIt']").click()
    

    time.sleep(1)
    try:
        
        XPATH = "//img[@title='" +book+ "']"
        imageclick = driver.find_element_by_xpath(XPATH).click()
        time.sleep(1)
        # AR = driver.findElement(By.xpath("//span[@id='email-display']")).click()
        AR = driver.find_element_by_xpath("//span[@id='ctl00_ContentPlaceHolder1_ucBookDetail_lblPoints']").text
        
        
        print(book)
    except NameError and NoSuchElementException:
        
        print(book)
        
    #LEX part
    driver.get("https://hub.lexile.com/find-a-book/search")
    driver.find_element_by_xpath("//input[@id='downshift-0-input']").send_keys(book)
    driver.find_element_by_xpath("//div[@class='sc-emDsmM sc-cBIieI iGlonI eiBpxY']//button[@type='submit'][normalize-space()='Search']").click()
    time.sleep(1)
    try:
        # XPATH = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/main[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]"
        # driver.find_elements_by_xpath(XPATH).click()
        time.sleep(1)
        Lex = driver.find_element_by_xpath("//div[@class='sc-bQFuvY hhiLNY']").text
        driver.quit()
    except AttributeError:
        driver.quit()
    
    dic[book] = (AR,Lex)
    print(dic)