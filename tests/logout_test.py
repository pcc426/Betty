#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 6/28/17


import sys
import time
import unittest
from appium import webdriver
from wheel.signatures import assertTrue
import DriverConfig


class MyTestCase(unittest.TestCase):
    """Here comes comments"""

    def setUp(self):
        pass

    def test_logout(self):
        # 跳过广告
        time.sleep(10)
        # 第二种方法使用缓慢拖动swipe来拖动屏幕，duration表示持续时间
        self.driver.swipe(start_x=0, start_y=1500, end_x=0, end_y=550, duration=1000)

if __name__ == '__main__':
    unittest.main()
