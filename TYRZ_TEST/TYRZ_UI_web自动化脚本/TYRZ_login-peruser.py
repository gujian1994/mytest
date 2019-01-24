# coding = utf-8
from selenium import webdriver
import time
import unittest


# 登录统一认证账户中心
from selenium.webdriver.chrome.webdriver import WebDriver


class Test_sure(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://61.190.70.197:8802/uccp-server/login')
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        print('test the start ')
    def tearDown(self):
        print('test the end ')

class TYRZ_login(Test_sure):
    def test_per_login(self):
        self.driver.find_element_by_id('perName').send_keys('340222199108160013')
        self.driver.find_element_by_id('perPsd').send_keys('qqqq1111')
        self.driver.find_element_by_id('psdBtn').click()
        self.driver.implicitly_wait(5)
        self.text1 = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/div[1]/span').text
        print(text1)

    def test_leg_login(self):
        self.driver.find_element_by_id('legal').click()
        self.driver.find_element_by_id('legUserName').send_keys('91340700151112130R')
        self.driver.find_element_by_id('legPsd').send_keys('qqqq2222')
        self.driver.find_element_by_id('legalpsdBtn').click()
        self.driver.implicitly_wait(5)
        text2 = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/div[1]/span').text
        print(text2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TYRZ_login("test_per_login"))
    suite.addTest(TYRZ_login("test_leg_login"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
