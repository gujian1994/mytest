import os
from time import sleep
import HTMLTestRunner
import unittest
from appium import webdriver


class Login (unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'PBV5T16928003673',
                        'appPackage': '自己的包名',
                        'appActivity': 'activity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(2)
        # 跳过展示页
        try:
            ima1 = self.driver.find_element_by_class_name("android.widget.ImageView")
            if ima1:
                self.driver.swipe(1000, 1500, 200, 1500, 1000)
                self.driver.implicitly_wait(5)

            ima2 = self.driver.find_element_by_class_name("android.widget.ImageView")
            if ima2:
                self.driver.swipe(1000, 1500, 200, 1500, 1000)
            self.driver.implicitly_wait(5)

            ima3 = self.driver.find_element_by_class_name("android.widget.ImageView").click ()

        except (Exception,e):
            print(e)

        # 设置权限
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.xihe.moblie.credit:id/goto_settings").click ()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click ()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click ()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click ()
        self.driver.implicitly_wait(20)

    def test_login(self):

        try:
            el = self.driver.find_element_by_id("com.xihe.moblie.credit:id/ll_homeme")

            if el:
                el.click()
        except (Exception, e):
            print('an element could not find')
            print(e)
        sleep(5)
        self.driver.find_element_by_id("com.xihe.moblie.credit:id/et_account").send_keys ('自己的手机号')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.xihe.moblie.credit:id/et_password").send_keys ('密码')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.xihe.moblie.credit:id/btn_send_data").click ()
        a = self.driver.find_element_by_id("com.xihe.moblie.credit:id/tv_loan_history")
        b = self.driver.find_element_by_id("com.xihe.moblie.credit:id/tv_instructions")
        self.assertEquals(a.text, u'借款记录')
        self.assertIn(u'验证是否是自己的名字', b.text)
        sleep(10)

    def test_logout(self):
        global e
        try:
            self.test_login ()
            self.driver.find_element_by_id("com.xihe.moblie.credit:id/ll_homeme").click ()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.xihe.moblie.credit:id/ll_seting").click ()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.xihe.moblie.credit:id/btn_out_user").click ()
            self.driver.implicitly_wait(5)
            e = self.driver.find_element_by_id("com.xihe.moblie.credit:id/tv_application_amount").text
            self.assertEqual('500', e)
        except (Exception, e):
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # # suite=unittest.makeSuite(DemoPage)
    # 构造测试集
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Login("test_login"))
        suite.addTest(Login("test_logout"))
        return suite


    # 定义报告存放路径，支持相对路径
    filename = "result.html"
    fp = file(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'薪动钱包测试报告', description=u' 用例执行情况：')

    # 运行测试用例
    runner.run(suite())
    fp.close()
