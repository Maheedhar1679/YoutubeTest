import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://realpython.com/")
driver.maximize_window()
driver.find_element("xpath","//a[@class='nav-link rounded mx-0 px-lg-2']").click()
driver.find_element("xpath","//input[@type='email']").send_keys("maheedharsaisubramanyam@gmail.com")
driver.find_element("xpath","//input[@type='password']").send_keys("Mahi@8500")
#action chains with wait
actions = ActionChains(driver)
ele= driver.find_element("xpath","//button[@type='submit']");
actions.move_to_element(ele).perform()
ele.click()
act_title = driver.title
exp_title = "Python Tutorials – Real Python"
if (act_title == exp_title):
    print("login test passed")
else:
    print("login test failed")
print(driver.title)
#dropdown
time.sleep(20)
element = driver.find_element("xpath","(//a[@role='button'])[1]")
actions.move_to_element(element).perform()
element.click()

time.sleep(20)
driver.quit()
