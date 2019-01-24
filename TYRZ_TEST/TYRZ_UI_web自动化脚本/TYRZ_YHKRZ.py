# coding = utf-8
from selenium import webdriver
import time
import os
import unittest
from selenium.common.exceptions import NoSuchElementException

'''
登录统一认证账户中心
'''

driver = webdriver.Chrome()
driver.get("http://61.190.70.197:8800/uccp-server/login")
time.sleep(1)
driver.maximize_window()
title = driver.title
driver.find_element_by_id('perName').send_keys('342601199406200214')
#341103198612283049 孙长如
driver.find_element_by_id('perPsd').send_keys('qqqq1111')
driver.find_element_by_id('psdBtn').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="hkRZManager"]/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/span/span[1]/span/input').send_keys('6217920404935053')
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div/span/span[1]/span/input').send_keys('18656986816')
a = input("请输入图形验证码:")
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[4]/div/span/div[1]/span[1]/span/input').send_keys(a)
driver.find_element_by_xpath('//*[@id="bankphoneDynamic"]').click()
b = input('请输入短信验证码:')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="bankmsgDynamic"]').send_keys(b)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div/div/button[1]').click()
c = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]').text
class BankCase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(c,'初级认证',msg="未完成银行卡认证")
        pass
if __name__ == '__main__':
    unittest.TestCase()