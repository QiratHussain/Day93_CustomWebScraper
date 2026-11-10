from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# PRODUCT= input("Which product do you wanna research: ")
PRODUCT= "Shoes"
driver= Driver(uc=True)
driver.get( "https://www.daraz.pk")
time.sleep(3)
search_input= driver.find_element(By.NAME,"q")
search_input.click()
search_input.send_keys(PRODUCT, Keys.ENTER)
time.sleep(2)


# TODO: 2. ask user product nam
# TODO: 3. search the product on daraz.com
# TODO: 4. fetch the products titles, hrefs and prices
time.sleep(300)
driver.quit()