from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class makeScreen:
    def scrnsht(self):
        driver = webdriver.Chrome()
        driver.get("https://vk.com/")
        time.sleep(2)
        button = driver.find_element(By.XPATH,"//button[@type='submit']//span[@class='FlatButton__in']")
        button.screenshot(".\\web.png")
        button.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Users\\mahee\\Downloads\\Sample\\web.png")
        driver.save_screenshot(".\\thirdscreen.png")
a = makeScreen()
a.scrnsht()