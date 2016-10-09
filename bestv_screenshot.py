# -*- coding: UTF-8 -*-

import os
from appium.webdriver.common.touch_action import TouchAction
import unittest
from appium import webdriver
import time

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class BestvScreenshotAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = 'Default'
        desired_caps['deviceName'] = 'EUQKCUIBE6RKPNTG'
        # 不重置app
        desired_caps['noReset'] = 'True'
        # 重置app时取注销下行并替换apk
        # desired_caps['app'] = os.path.abspath('/../../../Betty/apps/Bestv_20160927_2.2.1_update_dev_r0.apk')
        desired_caps['appPackage'] = 'com.bestv.app'
        desired_caps['appActivity'] = 'com.bestv.app.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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