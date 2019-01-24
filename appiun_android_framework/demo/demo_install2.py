import os
from appium import webdriver

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {"platformName":"Android",
                "deviceName":"127.0.0.1:62001",
                "platformVersion":"6.0",
                "appPackage":"com.iflytek.oshall.ceshi",
                "appActivity":"com.iflytek.oshall.bsdt.activity.WelcomeActivity"}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
