# coding = utf-8
from typing import List, Any, Union

from selenium import webdriver
import time
import unittest

'''
个人注册--身份证注册
'''
driver = webdriver.Chrome()
driver.get("http://61.190.70.197:8800/uccp-user/resources/register/register")
driver.maximize_window()
#sreach_windows = driver.current_window_handle
time.sleep(2)

#driver.find_element_by_xpath('//*[@id="userLogin"]/li[6]/a[2]').click()
'''
all_handles = driver.windows_handle
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
    driver.switch_to.windows(handle)
    print('new register window')
'''
time.sleep(4)
driver.find_element_by_css_selector("#form2 > div > div:nth-child(3) > div.form-control > span > span.widget.textbox.pf5.input > span > input").send_keys('340402197903280416')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="form2"]/div/div[5]/div/span/span[1]/span/input').send_keys('沈善武')
driver.find_element_by_xpath('//*[@id="form2"]/div/div[6]/div/div/span/span/span[1]').click()
driver.find_element_by_xpath('//*[@id="sex_listbox"]/li[1]').click()
driver.find_element_by_xpath('//*[@id="form2"]/div/div[7]/div/div/span/span/input').send_keys("汉族")
time.sleep(2)

driver.find_element_by_id('inputPwd').send_keys('qqqq1111')
driver.find_element_by_name('password2').send_keys('qqqq1111')
driver.find_element_by_name('mobilePhone').send_keys('13400000001')
time.sleep(10)
n = input ('输入图形验证码')
driver.find_element_by_name('verifyCode').send_keys(n)
driver.find_element_by_xpath('//*[@id="phoneDynamic"]').click()
y = input('输入短信验证码')
time.sleep(10)
driver.find_element_by_id('msgDynamic').send_keys(y)
driver.find_element_by_id('realNameXy').click()
#driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div[2]/div[2]/button[1]').click
#driver.quit()

