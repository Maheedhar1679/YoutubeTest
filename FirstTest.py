import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://realpython.com/")
driver.maximize_window()

# Wait for the login button and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link rounded mx-0 px-lg-2']"))
)
login_button.click()

# Wait for the email input and fill it
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
)
email_input.send_keys("maheedharsaisubramanyam@gmail.com")

# Fill in the password
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys("Mahi@8500")

# Wait for the submit button and hover over it
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

# Create ActionChains and perform hover, then click the button
actions = ActionChains(driver)
actions.move_to_element(submit_button).perform()

# Click the button
submit_button.click()

# Sleep for 20 seconds to see the result (if needed)
time.sleep(20)

# Close the browser
driver.quit()

#dropdown
dropdown_element = driver.find_element("xpath","//a[@role='button']")
dropdown = Select(dropdown_element)
all_options = dropdown.options
for index, option in enumerate(all_options):
    if index == 1:
        option.click()
        print(f"Selected option: {option.text}")
        break

