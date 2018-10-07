import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("C:\\Users\\owner\\Downloads\\chromedriver_win32\\chromedriver")
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Selenium Python Interview Questions")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

# assert "No results found." not in driver.page_source
# driver.refresh()
driver.close()

print("Test Completed")

time.sleep(4)
driver.quit()