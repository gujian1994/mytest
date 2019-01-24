# coding = utf-8
from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver

'''
登录统一认证账户中心
'''
driver: WebDriver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.get("http://61.190.70.197:8800/uccp-server/login")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_id('legal').click()
driver.find_element_by_id('legUserName').send_keys('91340700151112130R')
driver.find_element_by_id('legPsd').send_keys('qqqq2222')
driver.find_element_by_id('legalpsdBtn').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[3]/a').click()

driver.find_element_by_name('oldPassword').send_keys("qqqq2222")
driver.find_element_by_name('newPassword').send_keys("qqqq1111")
driver.find_element_by_name('newPassword2').send_keys("qqqq1111")

#driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div/div/div/span').click()
# ------------------------------------------修改基本信息-----------------------------------------------
driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[2]/a').click()
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/span').click()
driver.find_element_by_name('telephone').clear()
driver.find_element_by_name('telephone').send_keys('18800000000')
T = driver.find_element_by_name('telephone').text
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('gujiandidi11@qq.com')
E = driver.find_element_by_name('email').text
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/span[1]').click()
time.sleep(2)
print(T)

'''
class assert_name(unittest.TestCase):
    def test_modify_jbxx(self):
        self.assertEqual(T, '18800000011')

    def test_modify_jbxx2(self):
        self.assertEqual(E, 'gujiandidi@qq.com')
    pass


if __name__ == '__main__':
        unittest.main()

# driver.quit()
'''