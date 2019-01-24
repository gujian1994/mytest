# coding = utf-8
from selenium import webdriver
import time
import os
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
class HBSJtestcres(unittest.TestCase):
    def test_HBSJ(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://-- />-user/resources/accountAppeal/artAppel')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="form2"]/div[1]/div[3]/div/span/span[1]/span/input').send_keys('342601199406200214')
        self.driver.find_element_by_xpath('//*[@id="form2"]/div[1]/div[4]/div/span/span[1]/span/input').send_keys('顾健')
        self.driver.find_element_by_xpath('//*[@id="problemDesc"]').send_keys('测试')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[3]/div[2]/div/span[1]/span/input').send_keys('18100000008')
        a = input("请输入图形验证码：")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[3]/div[3]/div/span/div[1]/span[1]/span/input').send_keys(a)
        self.driver.find_element_by_xpath('//*[@id="phoneDynamic"]').click()
        b = input("请输入短信验证码：")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="msgDynamic"]').send_keys(b)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[4]/div').click()
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="uploadAgentImg"]').click()
        os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="uploadImgIdCard1"]').click()
        os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="uploadImgIdCard2"]').click()
        os.system("C:\\Users\\admin\Desktop\\uploadFile.exe")
        time.sleep(15)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[4]/div[3]/div[1]').click()
if __name__ == '__main__':
    unittest.main()






