import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"]='127.0.0.1:62001'
        desired_caps['browserName'] = ''
        #desired_caps['version'] = '4.4.2
        desired_caps["platformVersion"] = "23.0"
        #PATH('D:\\untitled\\appiun_android_framework\\app\\0116_ceshi_debug.apk')
        desired_caps["appPackage"]="com.iflytek.oshall.ceshi"
        desired_caps["appActivity"]="com.iflytek.oshall.bsdt.activity.WelcomeActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_login1(self):
        button = self.driver.find_element_by_id("com.subject.zhongchou:id/register_button")
        button.click()
        time.sleep(5)
        # 登录
        name = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_phone')
        name.click()
        name.send_keys('18656986816')

        psd = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_password')
        psd.click()
        psd.send_keys('qqqq1111')

        blogin = self.driver.find_element_by_id('com.subject.zhongchou:id/go_numberlogin')
        blogin.click()
        time.sleep(10)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginAndroidTests("test_login1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)