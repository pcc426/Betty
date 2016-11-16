# -*- coding: UTF-8 -*-

import os
from appium.webdriver.common.touch_action import TouchAction
import unittest
from appium import webdriver
from time import sleep
from bestv_config import WebDriverConfig

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class BestvSampleAndroidTests(unittest.TestCase):
    def setUp(self):
        config = WebDriverConfig()
        # config.start_Appium('127.0.0.1','4723','4723')
        sleep(10)
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = 'Default'
        # 更换真机测试时需变更deviceName
        # desired_caps['deviceName'] = 'CJL5T15B18017891'
        desired_caps['deviceName'] = 'Android Emulator'
        # 不重置app
        # desired_caps['noReset'] = 'True'
        # 重置app时取注销下行并替换apk
        desired_caps['app'] = os.path.abspath('C:\Users\p\Projects\Betty\\apps\\bestv_v2.2.2_update_ceshi_20161107.apk')
        desired_caps['appPackage'] = 'com.bestv.app'
        desired_caps['appActivity'] = 'com.bestv.app.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_element(self):
        # 等待广告
        sleep(10)
        self.driver.find_element_by_xpath('//android.widget.Button[@text == u"直播"]').click()
        sleep(2)

    def test_swipe_splash(self):
        #等待广告
        sleep(10)
        #连续滑动
        self.driver.swipe(start_x=800, start_y=1000, end_x=100, end_y=1000, duration=1000)
        sleep(1)
        self.driver.swipe(start_x=800, start_y=1000, end_x=100, end_y=1000, duration=1000)
        sleep(1)
        self.driver.swipe(start_x=800, start_y=1000, end_x=100, end_y=1000, duration=1000)
        sleep(1)
        self.driver.swipe(start_x=800, start_y=1000, end_x=100, end_y=1000, duration=1000)
        sleep(1)
        self.driver.swipe(start_x=800, start_y=1000, end_x=100, end_y=1000, duration=1000)

    def test_swipe(self):
        # 跳过广告
        sleep(10)
        # 第二种方法使用缓慢拖动swipe来拖动屏幕，duration表示持续时间
        self.driver.swipe(start_x=0, start_y=1500, end_x=0, end_y=550, duration=1000)
if __name__ == '__main__':
     suite = unittest.TestLoader().loadTestsFromTestCase(BestvSampleAndroidTests)
     unittest.TextTestRunner(verbosity=2).run(suite)