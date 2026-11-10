from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

PRODUCT= input("Which product do you wanna research: ")

driver= Driver(uc=True)
driver.get( "https://www.daraz.pk")
time.sleep(3)
search_input= driver.find_element(By.NAME,"q")
search_input.click()
search_input.send_keys(PRODUCT, Keys.ENTER)
time.sleep(2)
products= driver.find_elements(By.CLASS_NAME,"Bm3ON")
if products:
    for product in products:
        title= product.find_element(By.CLASS_NAME,"RfADt").text
        price= product.find_element(By.CLASS_NAME,"ooOxS").text
        link= product.find_element(By.TAG_NAME,"a").get_attribute("href")
        try:
            with open(f"{PRODUCT}.csv",mode="a") as file:
                file.write(f"{title},{price}, {link} \n")
        except:
            with open (f'{PRODUCT}.csv', mode='w') as file:
                file.write(f"{title},{price}, {link}\n")


time.sleep(300)
driver.quit()
