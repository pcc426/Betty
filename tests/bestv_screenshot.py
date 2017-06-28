#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 4/21/17

import os
import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from tests.bestv_config import WebDriverConfig

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class BestvScreenshotAndroidTests(unittest.TestCase):
    def setUp(self):
        config = WebDriverConfig()
        config.setup_config()
        self.driver = webdriver.Remote(config.command_executor, config.desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_play_screenshot(self):
        # 等待广告
        time.sleep(20)
        # 切换频道
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '娱乐综艺')]").click()
        time.sleep(5)
        t1 = TouchAction(self.driver)
        # 通过坐标点击分类下banners
        t1.press(x=350, y=400).wait(1000).release().perform()
        time.sleep(15)
        # 保存截图到指定目录下
        try:
            self.driver.get_screenshot_as_file("screenshot_" + self._testMethodName + time.ctime() + ".png")
        except IOError:
            print IOError
        else:
            print "screenshot save successfully!"


if __name__ == '__main__':
     suite = unittest.TestLoader().loadTestsFromTestCase(BestvScreenshotAndroidTests)
     unittest.TextTestRunner(verbosity=2).run(suite)