# coding = utf-8
from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver

'''
个人忘记密码
'''
driver: WebDriver = webdriver.Chrome()
driver.get("http://61.190.70.197:8800/uccp-user/resources/legalPerson/forgetPsd/forgetPsd")
driver.maximize_window()
#sreach_windows = driver.current_window_handle
'''第一个填写登陆账号界面'''
time.sleep(2)
driver.find_element_by_xpath('//*[@id="forget-step1"]/div[1]/div/span[1]/span/input').send_keys('91340700151112130R')
n = input ("请输入图形验证码:")
driver.find_element_by_xpath('//*[@id="forget-step1"]/div[2]/div/div/div[1]/span/span/input').send_keys(n)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="forget-step1"]/div[3]/button[1]').click()
'''第二个验证身份界面'''
time.sleep(2)
driver.find_element_by_xpath('//*[@id="phoneDynamic"]').click()
a = input ("请输入短信验证码")
driver.find_element_by_xpath('//*[@id="forget-step2"]/div[1]/div[2]/div/div[1]/span/span/input').send_keys(a)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="stepTwo"]/button[1]').click()
'''第三个重新设置密码界面'''
time.sleep(2)
I = 'qqqq2222'
driver.find_element_by_xpath('//*[@id="inputText"]').send_keys(I)
driver.find_element_by_xpath('//*[@id="confirmPwd"]').send_keys(I)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="forget-step3"]/div[3]/button[1]').click()
driver.quit()