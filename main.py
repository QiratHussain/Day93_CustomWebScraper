from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINK= "https://www.daraz.pk/"
driver= Driver(uc=True)
driver.get(LINK)
search_input= driver.find_element(By.CSS_SELECTOR("#q"))
search_input.click()
driver.quit()

# TODO: 2. ask user product name
# TODO: 3. search the product on daraz.com
# TODO: 4. fetch the products titles, hrefs and prices