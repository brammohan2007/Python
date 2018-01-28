#!/usr/bin/env python


import os
import re
import requests
from selenium import webdriver
import time
import unittest
class Testing(unittest.TestCase):

    def setUp(self):
        
        self.url = "http://www.thomasbayer.com/sqlrest/CUSTOMER/"
        self.chromedriver = "C:/Users/vdusari/Downloads/chromedriver_win32/chromedriver"
        os.environ["webdriver.chrome.driver"] = self.chromedriver

    def test_url(self):
        req = requests.request('GET', self.url)
        self.assertEqual(req.status_code,200)
        # print("content {0}".format(req.content))

    def test_sel(self):
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)
        self.driver.get("https://www.w3schools.com/")
        self.assertEqual(self.driver.title,"W3Schools Online Web Tutorials")
        self.driver.close()

    def test_form(self):
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)
        self.driver.get("http://www.practiceselenium.com/practice-form.html")
        form = self.driver.find_element_by_tag_name("form")
        form.find_element_by_name("firstname").send_keys("sone")
        form.find_element_by_name("lastname").send_keys("Lone")
        form.find_element_by_id("datepicker").send_keys("25-01-2018")
        form.find_element_by_id("tea2").click()
        form.find_element_by_id("tool-1").click()
        form.submit()
        self.assertEqual(self.driver.title,"Welcome")
        self.driver.close()

    def test_tab(self):
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)
        self.driver.get("http://www.seleniumframework.com/Practiceform/")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div/div[1]/div/p[4]/button").click()
        # To Switch second window
        self.assertEqual(self.driver.title,'Selenium Framework | Practiceform')
        if len(self.driver.window_handles) > 1:
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.title,'Selenium Framework | Selenium, Cucumber, Ruby, Java et al.')
        # self.driver.close()

    def test_json(self):
        import json
        m = {'a':1,'b':2,'c':3}
        n = json.dumps(m)
        o = json.loads(n)
        for eachkey in o.keys():
            self.assertIn(eachkey,['a', 'b', 'c'])
        for eachvalue in o.values():
            self.assertIn(eachvalue,[1, 2, 3])
        self.assertEqual(o['c'],3)

    def test_db(self):
        import sqlite3
        conn = sqlite3.connect('emp.db')
        cursor = conn.execute("select * from emp1")
        for eachrow in cursor:
            self.assertIn(eachrow,[('ramu', '123', 'hyd'),('mohan', '432', 'che')])
        conn.close()

    def tearDown(self):
        pass
        # self.driver.close()

if __name__ == "__main__":
    unittest.main()