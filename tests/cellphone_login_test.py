# -*- coding: UTF-8 -*-

import os
import time
import unittest
import sys

from appium import webdriver
from wheel.signatures import assertTrue

from lib.DriverConfig import WebDriverConfig

# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class CellphoneLoginTests(unittest.TestCase):

    def setUp(self):
        # print sys.path + '\n'
        config = WebDriverConfig()
        config.setup_config()
        self.driver = webdriver.Remote(config.command_executor, config.desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_telephone_login(self):
        # 等待广告
        time.sleep(10)
        print('CURRENT ACTIVITY=' + self.driver.current_activity)
        self.driver.find_element_by_xpath('//android.widget.Button[@text = "我的"]').click()
        time.sleep(2)
        el = self.driver.find_element_by_id('loginbtn')
        if el.text == u"点击登录":
            # 未登录状态
            pass
        else:
            # 已登录状态下退出登录
            self.driver.find_element_by_id('btn_right').click()
            time.sleep(2)
            self.driver.find_element_by_id('logout_btn').click()
            time.sleep(2)
            self.driver.find_element_by_id('dlg_btn_ok').click()
            time.sleep(2)
            # 退出登录后点击返回
            self.driver.keyevent(4)
        el.click()
        time.sleep(2)

        # 输入手机号/密码
        phone_number = '18601750451'
        pwd = '750451'
        self.driver.find_element_by_id('phone_edit').send_keys(phone_number)
        self.driver.find_element_by_id('pwd_edit').send_keys(pwd)
        # 滑动页面,让[登录]按钮露出
        self.driver.swipe(start_x=0, start_y=850, end_x=0, end_y=350, duration=1000)
        # self.driver.keyevent(66) #键盘输入ENTER, 对部分定制键盘的Android机型无效
        # 点击登录按钮
        self.driver.find_element_by_id('login_btn').click()
        time.sleep(5)

        el = self.driver.find_element_by_id('loginbtn')
        assertTrue(el.text != u'点击登录')


    # def test_logout(self):
    #     # 跳过广告
    #     sleep(10)
    #     # 第二种方法使用缓慢拖动swipe来拖动屏幕，duration表示持续时间
    #     self.driver.swipe(start_x=0, start_y=1500, end_x=0, end_y=550, duration=1000)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CellphoneLoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
