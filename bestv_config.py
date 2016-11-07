# -*- coding: UTF-8 -*-

# from appium import webdriver
# from appium import WebDriver
import os


class WebDriverConfig(object):

    def __init__(self):
        self.desired_capabilities = {}
        self.command_executor = 'http://localhost:4723/wd/hub'

    def setup_config(self):
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = 'Default'
        # 更换真机测试时需变更deviceName
        # desired_caps['deviceName'] = '23e74656'
        desired_caps['deviceName'] = 'Nexus_5_Android_6_0'
        # 不重置app
        # desired_caps['noReset'] = 'True'
        # 重置app时取注销下行并替换apk路径
        desired_caps['app'] = os.path.abspath('/Users/pcc/Betty/apps/bestv_v2.2.2_update_ceshi_20161023175936.apk')
        # desired_caps['app'] = '/../apps/bestv_v2.2.2_update_ceshi_20161023175936.apk'
        desired_caps['appPackage'] = 'com.bestv.app'
        desired_caps['appActivity'] = 'com.bestv.app.activity.MainActivity'
        self.desired_capabilities = desired_caps
