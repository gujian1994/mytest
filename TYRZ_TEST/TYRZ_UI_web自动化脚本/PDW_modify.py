# coding = utf-8
import TYRZ_TEST
from selenium import webdriver
import time
import unittest

class Test_TYRZ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://61.190.70.197:8800/uccp-server/login')
        self.driver.maximize_window()
        print('test the start')
    def tearDown(self):
        print('test the end')

class MyTest1(Test_TYRZ):
    def test_PWD_modify_legal(self):
        self.driver.find_element_by_id('legal').click()
        self.driver.find_element_by_id('legUserName').send_keys('91340700151112130R')
        self.driver.find_element_by_id('legPsd').send_keys('qqqq2222')
        self.driver.find_element_by_id('legalpsdBtn').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[3]/a').click()
        self.driver.find_element_by_name('oldPassword').send_keys("qqqq2222")
        self.driver.find_element_by_name('newPassword').send_keys("qqqq1111")
        self.driver.find_element_by_name('newPassword2').send_keys("qqqq1111")
        #self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div/div/div/span').click()
class MyTest2(Test_TYRZ):
    def test_PWD_modify_per(self):
        self.driver.find_element_by_id('perName').send_keys('341103198612283049')
        self.driver.find_element_by_id('perPsd').send_keys('qqqq1111')
        self.driver.find_element_by_id('psdBtn').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[3]/a').click()
        self.driver.find_element_by_name('oldPassword').send_keys("qqqq1111")
        self.driver.find_element_by_name('newPassword').send_keys("qqqq2222")
        self.driver.find_element_by_name('newPassword2').send_keys("qqqq2222")
        #self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div/div/div/span').click()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest1("test_PWD_modify_legal"))
    suite.addTest(MyTest2("test_PWD_modify_per"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
