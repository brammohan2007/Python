from selenium import webdriver
import unittest
import os


class Html(unittest.TestCase):

    def test_html_a(self):
        self.driver = webdriver.Chrome(
            "C:/Users/rbandapalli/Documents/GitHub/python/chromedriver_win32/chromedriver.exe"
        )
        # os.environ["webdriver.chrome.driver"] = self.driver
        self.driver.get("http://www.inmar.com")
        elements = self.driver.find_elements_by_tag_name('a')
        for each in elements:
            if each.get_attribute("href") and each.get_attribute("href").startswith("https"):
                print(each.get_attribute("href"))

if __name__=="__main__":
    unittest.main()


