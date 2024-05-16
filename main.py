"""
Making In-person appointments only for now at SCC
Basics: Making an appointment for [Consortium]
To Do: Scrape the data and search for "Counselors" and "Times available"
"""
# importing necessary packages 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
XPath Cheat Sheet = "https://quickref.me/xpath"
SCC Counseling = "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp?WCI=Init&WCE=Settings"
"""

# for holding the resultant list 
page_url = "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp"
options = Options()
options.add_experimental_option("detach", True) # So browser don't close prematurely
driver = webdriver.Chrome(options=options)
driver.get(page_url)

# use for test data
student_id = "W2056162"
dob = "02/01/2005" 
counseling_reason = "Consortium"

# finding the  input boxes for 1st page
enter_student_id = driver.find_element(By.XPATH, '//*[@id="ssn"]')
enter_dob = driver.find_element(By.XPATH, '//*[@id="dob"]')
sign_in_button = driver.find_element(By.XPATH, '//*[@id="cmdContinue"]')

# Enter the information
""" 
Variables:
student_id : string
dob        : string
"""
enter_student_id.clear()
enter_student_id.send_keys(student_id)

enter_dob.clear()
enter_dob.send_keys(dob)

sign_in_button.click()

# Page 2 ----------------------------------------------------------------

# Make an appointment for a specific reason
""" 
Variables:
counseling_reason : string
"""
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID, "cmdMakeAppt"))
)
driver.find_element(By.ID, "cmdMakeAppt").click()
driver.find_element(By.XPATH, "/html/body/div[@class='table-container']/form[@id='frmReason']/div[@class='center-block margin-top']/select[@id='reason']/option[2]").click()
driver.find_element(By.XPATH, "/html/body/div[@class='table-container']/form[@id='frmReason']/div[@class='center-block']/button[@id='cmdContinue']").click()

# Page 3, need to check for appointments available ---------------------