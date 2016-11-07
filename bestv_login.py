# -*- coding: UTF-8 -*-

import os
from appium.webdriver.common.touch_action import TouchAction
import unittest
from appium import webdriver
from time import sleep
from bestv_config import WebDriverConfig
from wheel.signatures import assertTrue

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class BestvLoginAndroidTests(unittest.TestCase):
    def setUp(self):
        config = WebDriverConfig()
        config.setup_config()
        self.driver = webdriver.Remote(config.command_executor, config.desired_capabilities)


    def tearDown(self):
        self.driver.quit()

    def test_telephone_login(self):
        # 等待广告
        sleep(10)
        self.driver.find_element_by_xpath('//android.widget.Button[@text = "我的"]').click()
        sleep(2)
        el = self.driver.find_element_by_id('loginbtn')
        if el.text == u"点击登录":
            # 未登录状态
            pass
        else:
            # 已登录状态下退出登录
            self.driver.find_element_by_id('btn_right').click()
            sleep(2)
            self.driver.find_element_by_id('logout_btn').click()
            sleep(2)
            self.driver.find_element_by_id('dlg_btn_ok').click()
            sleep(2)
            # 退出登录后点击返回
            self.driver.keyevent(4)
        el.click()
        sleep(2)

        # 输入手机号/密码
        phone_number = '18601750455'
        pwd = 'bestv2016'
        self.driver.find_element_by_id('phone_edit').send_keys(phone_number)
        self.driver.find_element_by_id('pwd_edit').send_keys(pwd)
        # 滑动页面,让[登录]按钮露出
        self.driver.swipe(start_x=0, start_y=850, end_x=0, end_y=350, duration=1000)
        # self.driver.keyevent(66) #键盘输入ENTER, 对部分定制键盘的Android机型无效
        # 点击登录按钮
        self.driver.find_element_by_id('login_btn').click()
        sleep(5)

        el = self.driver.find_element_by_id('loginbtn')
        assertTrue(el.text != u'点击登录')

    def test_weixin_login(self):
        pass  #to-do

    def test_qq_login(self):
        pass  #to-do

    # def test_logout(self):
    #     # 跳过广告
    #     sleep(10)
    #     # 第二种方法使用缓慢拖动swipe来拖动屏幕，duration表示持续时间
    #     self.driver.swipe(start_x=0, start_y=1500, end_x=0, end_y=550, duration=1000)

if __name__ == '__main__':
     suite = unittest.TestLoader().loadTestsFromTestCase(BestvLoginAndroidTests)
     unittest.TextTestRunner(verbosity=2).run(suite)