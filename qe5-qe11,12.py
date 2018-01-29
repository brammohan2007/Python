#!/usr/bin/env python


import os
import re
import json
import sqlite3
import requests
from selenium import webdriver
import time
import unittest

class Testing(unittest.TestCase):

    def setUp(self):
        self.url = "http://www.thomasbayer.com/sqlrest/CUSTOMER/"
    
    def test_url(self):
        req = requests.request('GET', self.url)
        self.assertEqual(req.status_code,200)
        
    def test_json(self):
        m = {'a':1,'b':2,'c':3}
        n = json.dumps(m)
        o = json.loads(n)
        for eachkey in o.keys():
            self.assertIn(eachkey,['a', 'b', 'c'])
        for eachvalue in o.values():
            self.assertIn(eachvalue,[1, 2, 3])
        self.assertEqual(o['c'],3)

    def test_db(self):
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