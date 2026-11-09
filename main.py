from seleniumbase import Driver

LINK= "https://www.daraz.pk/"
driver= Driver(uc=True)
driver.get(LINK)
driver.quit()

# TODO: 2. ask user product name
# TODO: 3. search the product on daraz.com
# TODO: 4. fetch the products titles, hrefs and prices