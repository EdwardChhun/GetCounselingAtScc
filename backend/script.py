from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from datetime import datetime
import time
import watchdog

"""
XPath Cheat Sheet = "https://quickref.me/xpath"
SCC Counseling = "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp"
"""

class WebBot():
    
    def __init__(self):
        
        print("Initializing WebBot...")
        
        options = Options()
        options.add_experimental_option("detach", True) # So browser don't close prematurely
        self.driver = webdriver.Chrome(options=options)
        
        print("Initialized finished...")
        
    def automate(self):
        
        driver = self.driver
        
        print("Reading data...")
        
        with open('../client/public/student_info.json') as f:
            data = json.load(f)
        
        student_id = data['id']
        dob = data['dob']
        email = data['email']
        counseling_reason = data['counselingReason']
        
        # Reformatting the date
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        dob_formatted = dob_date.strftime('%m/%d/%Y')
        
        print("Opening web page...")
        
        self.driver.get("https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp")
        
        print("Open web page successful...")
        
        print("Automation starting...")
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
        try:
            # Locate the input boxes on the first page
            enter_student_id = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ssn"]'))
            )
            enter_dob = self.driver.find_element(By.XPATH, '//*[@id="dob"]')
            sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="cmdContinue"]')
            
            print("Found elements on page 1...")

            # Enter the information
            enter_student_id.clear()
            enter_student_id.send_keys(student_id)
            time.sleep(1)

            enter_dob.clear()
            enter_dob.send_keys(dob_formatted)
            time.sleep(1)

            sign_in_button.click()
            time.sleep(1)

        except Exception as e:
            print(f"Error on page 1: {e}")
            self.driver.quit()
            return

        # Page 2 ----------------------------------------------------------------
        # Make an appointment for a specific reason
        """ 
        Variables:
        counseling_reason : string
        """
        try:
            # Make an appointment for a specific reason
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "cmdMakeAppt"))
            ).click()
            time.sleep(1)
            
            # Select the counseling reason from the dropdown
            select_reason = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[@id='reason']/option[{counseling_reason}]"))
            )
            select_reason.click()
            time.sleep(1)
            
            self.driver.find_element(By.XPATH, "//button[@id='cmdContinue']").click()
            time.sleep(1)

            # Add the rest of the necessary steps here for Page 3 and beyond
            # ...

        except Exception as e:
            print(f"Error on page 2: {e}")
            self.driver.quit()
            return
        
        print("Automation completed successfully!")
        self.driver.quit()
        # Page 3, need to check for appointments available ---------------------
        # Add the rest of the necessary steps here
        # ...
        
        
# Test run
 
if __name__ == "__main__":
    bot = WebBot()
    bot.automate()
    