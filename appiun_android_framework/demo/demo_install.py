import os
from appium import webdriver

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH(r"D:\untitled\appiun_android_framework\app\0116_ceshi_debug.apk")
desired_caps['appPackage'] = 'com.iflytek.oshall.ceshi'
desired_caps['appActivity'] = 'com.iflytek.oshall.bsdt.activity.WelcomeActivity'
self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)



