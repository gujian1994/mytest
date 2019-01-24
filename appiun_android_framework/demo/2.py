import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {}
desired_caps['device'] = 'android'
desired_caps["platformName"] = "Android"
desired_caps["deviceName"] = '127.0.0.1:62001'
desired_caps['browserName'] = ''
# desired_caps['version'] = '4.4.2
#desired_caps["platformVersion"] = "6.0"
# PATH('D:\\untitled\\appiun_android_framework\\app\\0116_ceshi_debug.apk')
desired_caps["appPackage"] = "com.iflytek.oshall.ceshi"
desired_caps["appActivity"] = "com.iflytek.oshall.bsdt.activity.WelcomeActivity"
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)
button = driver.find_element_by_class_name("android.widget.RelativeLayout")
button.click()