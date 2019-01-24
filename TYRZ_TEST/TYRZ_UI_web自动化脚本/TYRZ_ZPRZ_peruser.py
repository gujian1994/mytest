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
driver.find_element_by_id('perName').send_keys('341103198612283049')
driver.find_element_by_id('perPsd').send_keys('qqqq1111')
driver.find_element_by_id('psdBtn').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="hkRZManager"]/a').click()

sreach_window = driver.current_window_handle
a = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]').text
print(a)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div[3]/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="uploadImg1"]').click()
os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
time.sleep(7)
sreach_window = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="uploadImg2"]').click()
os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
time.sleep(7)
sreach_window = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="uploadImg3"]').click()
os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[4]/div/div/div/span[1]').click()
photo_name = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]').text
print(photo_name)
class photo(unittest.TestCase):
    def testcase(self):
        self.assertEqual(photo_name,'初级认证',msg="未完成照片认证上传")
        pass
if __name__ == '__main__':
    unittest.TestCase()
