from selenium import webdriver
driver_path=r'D:\\drivers\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.close()
