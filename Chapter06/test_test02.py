import unittest
from selenium import webdriver

class TestClass01(unittest.TestCase):

    def setUp(self):
        driver_path=r'D:\\drivers\\geckodriver.exe'
        driver = webdriver.Firefox(executable_path=driver_path)
        self.driver = driver
        print ("\nIn setUp()...")

    def tearDown(self):
        print ("\nIn tearDown")
        self.driver.close()
        self.driver.quit()

    def test_case01(self):
        print("\nIn test_case01()...")
        self.driver.get("http://www.python.org")
        assert self.driver.title == "Welcome to Python.org"

if __name__ == "__main__":
    unittest.main()
