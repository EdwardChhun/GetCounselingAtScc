# importing necessary packages 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.pinterest.com/ideas/")

# for holding the resultant list 
element_list = [] 

options = Options()
options.add_experimental_option("detach", True)
page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1"
driver = webdriver.Chrome(options=options) 
driver.get(page_url) 
title = driver.find_elements(By.CLASS_NAME, "title") 
price = driver.find_elements(By.CLASS_NAME, "price") 
description = driver.find_elements(By.CLASS_NAME, "description")    
rating = driver.find_elements(By.CLASS_NAME, "ratings") 
review_count = driver.find_elements(By.CLASS_NAME, "review-count")

for i in range(len(title)):
    element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text, review_count[i].text]) 

print(element_list) 

#closing the driver 
driver.close() 
