from selenium import webdriver
driver_path=r'D:\\drivers\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.close()
driver.quit()
