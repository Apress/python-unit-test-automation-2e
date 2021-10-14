from selenium import webdriver
import time

driver_path=r'D:\\drivers\\msedgedriver.exe'
driver = webdriver.Edge(executable_path=driver_path)

time.sleep(10)
driver.close()

time.sleep(5)
driver.quit()
