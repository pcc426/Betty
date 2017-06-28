# -*- coding: UTF-8 -*-

# __author__ = 'Chery Peng'

import configparser
import os
import sys

# sys.path.append('/Users/pcc/Betty/lib')


class DriverConfig(object):

    def __init__(self):
        self.desired_capabilities = {}
        self.command_executor = 'http://localhost:4723/wd/hub'
        self.file_path = os.path.abspath('./settings.conf')

    def setup_config(self):
        # file_path = os.path.abspath('../settings.conf')
        cp = configparser.ConfigParser()
        # cp.read(file_path)
        # print 'settings PATH=' + self.file_path
        cp.read(self.file_path)

        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = 'Default'
        # 更换真机测试时需变更deviceName
        desired_caps['deviceName'] = cp.get('devices', 'deviceName')
        # desired_caps['deviceName'] = 'Nexus_5_Android_6_0'
        # 不重置app
        desired_caps['noReset'] = cp.get('devices', 'noReset')
        # 重置app时取注销下行并替换apk路径
        desired_caps['app'] = os.path.abspath('./apps/' + cp.get('devices', 'apkName'))
        desired_caps['appPackage'] = 'com.bestv.app'
        desired_caps['appActivity'] = 'com.bestv.app.activity.MainActivity'
        self.desired_capabilities = desired_caps

    def get_file_path(self):
        return self.file_path

