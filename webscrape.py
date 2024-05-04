# importing necessary packages 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

"""
XPath Cheat Sheet = "https://devhints.io/xpath#operators"
"""

# for holding the resultant list 
element_list = [] 

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/EdwardChhun")

folder = driver.find_element_by_xpath('//span[@class="repo" and contains(text(), "Flappy-Bird-Game")]')
folder.click()




# options.add_experimental_option("detach", True)
# page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets"
# driver = webdriver.Chrome(options=options) 
# driver.get(page_url) 

# title = driver.find_elements(By.CLASS_NAME, "title") 
# price = driver.find_elements(By.CLASS_NAME, "price") 
# description = driver.find_elements(By.CLASS_NAME, "description")    
# rating = driver.find_elements(By.CLASS_NAME, "ratings") 
# review_count = driver.find_elements(By.CLASS_NAME, "review-count")

# for i in range(len(title)):
#     element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text, review_count[i].text]) 

# print(element_list) 

# #closing the driver 
# driver.close() 
