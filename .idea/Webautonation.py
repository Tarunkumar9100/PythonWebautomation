from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
time.sleep(5)

FirstName = driver.find_element_by_id("fname")
FirstName.send_keys("")

LastName = driver.find_element_by_id("lname")
LastName.send_keys("")

DateOfBirth = driver.find_element_by_id("dob")
DateOfBirth.send_keys("")

Email = driver.find_element_by_id("email")
Email.send_keys("")

Country = driver.find_element_by_id("country")
Country.send_keys("")

AboutYourself = driver.find_element_by_id("about")
AboutYourself.send_keys("")

Username = driver.find_element_by_id("username")
Username.send_keys("")

Password = driver.find_element_by_id("password")
Password.send_keys()

ConfirmPassword = driver.find_element_by_id("")
ConfirmPassword.send_keys("")

Iagree = driver.find_element_by_id("agree")
Iagree.click()

submit = driver.find_element_by_id("submit")
submit.click()

driver.switch_to.frame("IFrame without ID")

FirstName = driver.find_element_by_xpath("//*[@id='fname']")
FirstName.send_keys("")

LastName = driver.find_element_by_xpath("//*[@id='lname']")
LastName.send_keys("")

try:
    radiobutton = driver.find_element_by_xpath("//*[@id='radiobutton']")
except NoSuchElementException:
    print("Not Found")
else:
    Needtoclickgender = driver.find_element_by_xpath("//*[@id='Gender']")
    for button in radiobutton:
        if(button.get_attribute("value")==Needtoclickgender):
            button.click()

Username = driver.find_element_by_xpath("//*[@id='username']")
Username.send_keys("")

Password = driver.find_element_by_xpath("//*[@id='password']")
Password.send_keys("")

ConfirmPassword = driver.find_element_by_xpath("//*[@id='confirmpassword']")
ConfirmPassword.send_keys("")

Iagree = driver.find_element_by_xpath("//*[@id='agree")
Iagree.click()

submit = driver.find_element_by_id("submit")
submit.click()

driver.switch_to.frame("Nested iFrame Form")

FirstName = driver.find_element_by_xpath("//*[@name='First Name']")
FirstName.send_keys("")

LastName = driver.find_element_by_xpath("//*[@name='Last Name")
LastName.send_keys("")

Email = driver.find_element_by_xpath("//*[@name='Email']")
Email.send_keys("")

Hobbies = driver.find_element_by_xpath("//span[contains(text(),'Dance')]")
Hobbies.click()

driver.switch_to.frame("Inner Nested Form")

FirstName = driver.find_element_by_xpath("//*[@name='First Name")
FirstName.send_keys("")

LastName = driver.find_element_by_xpath("//*[@name='Last Name']")
LastName.send_keys("")

Email = driver.find_element_by_xpath("//*[@name='Email']")
Email.send_keys("")

driver.switch_to.default_content()

driver.switch_to.frame("")
