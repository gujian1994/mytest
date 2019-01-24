# coding = utf-8
from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver

'''
登录统一认证账户中心
'''
driver = webdriver.Chrome()
driver.get("http://61.190.70.197:8800/uccp-server/login")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id('legal').click()
driver.find_element_by_id('legUserName').send_keys('91340700151112130R')
driver.find_element_by_id('legPsd').send_keys('qqqq2222')
driver.find_element_by_id('legalpsdBtn').click()
time.sleep(3)
username = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/div[1]/span').text
print(username)
class assert_name(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(username,'111铜陵工程勘察院',msg='断言有误')
    pass

if __name__=='__main__':
        unittest.main()

#driver.quit()



