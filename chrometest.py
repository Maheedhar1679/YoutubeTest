from selenium import webdriver
from selenium.webdriver.common.by import By



def get_pet_details(K9-BD-01):

    driver = webdriver.Chrome()

    try:

        driver.get("https://petstore.octoperf.com/actions/Catalog.action")

        search_box = driver.find_element(By.NAME, "keyword")
        search_box.clear()
        search_box.send_keys(product_id)
        search_box.submit()

        product_link = driver.find_element(By.XPATH, "//a[contains(@href, 'Catalog.action?viewItem&itemId')]")
        product_link.click()

        #pet details
        product_name = drive
        product_breed = driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Breed')]/following-sibling::td").text  # Fetch the breed

        print(f"Product ID: {product_id}")
        print(f"Product Name: {product_name}")
        print(f"Breed: {product_breed}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the task
        driver.quit()


# Example usage
product_id = "FISH-001"  # Change this ID to test different products
get_pet_details(product_id)



