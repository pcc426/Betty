# -*- coding: UTF-8 -*-

# from appium import webdriver
# from appium import WebDriver


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
        desired_caps['deviceName'] = '860BCNM223DL'
        # 不重置app
        desired_caps['noReset'] = 'True'
        # 重置app时取注销下行并替换apk
        # desired_caps['app'] = os.path.abspath('/../../../Betty/apps/Bestv_20160927_2.2.1_update_dev_r0.apk')
        desired_caps['appPackage'] = 'com.bestv.app'
        desired_caps['appActivity'] = 'com.bestv.app.activity.MainActivity'
        self.desired_capabilities = desired_caps
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)