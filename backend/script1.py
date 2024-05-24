from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
XPath Cheat Sheet = "https://quickref.me/xpath"
SCC Counseling = "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp"
"""

class WebBot():
    
    def __init__(self, student_id, dob, counseling_reason):
        
        print("Initializing WebBot...")
        
        self.student_id = student_id
        self.dob = dob
        self.counseling_reason = counseling_reason
        self.driver = None
        
        print("-----------------")
        print(student_id)
        print(dob)
        print(counseling_reason)
        print("-----------------")
        
        print("Initialized finished...")
        
    def open_web_page(self):
        
        print("Opening web page...")
        
        # for holding the resultant list 
        page_url = "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp"
        options = Options()
        options.add_experimental_option("detach", True) # So browser don't close prematurely
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(page_url)
        
        print("Open web page successful...")
        
    def execute_web_bot(self):
        
        print("Executing bot...")
        
        driver = self.driver
        student_id = self.student_id
        dob = self.dob
        counseling_reason = self.counseling_reason
        
        # finding the  input boxes for 1st page
        enter_student_id = driver.find_element(By.XPATH, '//*[@id="ssn"]')
        enter_dob = driver.find_element(By.XPATH, '//*[@id="dob"]')
        sign_in_button = driver.find_element(By.XPATH, '//*[@id="cmdContinue"]')
        
        print("Found Elements...")

        # Page 1 ----------------------------------------------------------------
        # Enter the information
        """ 
        Variables:
        student_id : string
        dob        : string
        """
        enter_student_id.clear()
        enter_student_id.send_keys(student_id)
        time.sleep(1)

        enter_dob.clear()
        enter_dob.send_keys(dob)
        time.sleep(1)

        sign_in_button.click()
        time.sleep(1)

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
        time.sleep(1)
        driver.find_element(By.XPATH, f"//*[@id='reason']/option[{counseling_reason}]" ).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='cmdContinue']").click()
        time.sleep(1)

        # Page 3, need to check for appointments available ---------------------
        # Add the rest of the necessary steps here
        # ...
        
        
# Test run
 
if __name__ == "__main__":
    # use for test data
    student_id = "W2056162" #WiD
    dob = "02012005"        #MM/DD/YYYY 
    counseling_reason = 2   #Consortium
    
    bot = WebBot(student_id, dob, counseling_reason)
    bot.open_web_page()
    bot.execute_web_bot()
    