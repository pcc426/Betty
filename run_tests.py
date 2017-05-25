#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 4/21/17


import datetime
import getopt
import os
import sys
import unittest

import configparser

from lib import HTMLTestRunner

sys.path.append('./tests')


test_dir = './tests'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='user_login_test.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


def str2bool(v):
    return v.lower() in ('yes', 'true', 't', '1')


def main(argv):
    # device_name, apk_name, no_reset初始默认值
    device_name = 'CJL5T15B18017891'
    apk_name = 'bestv_v2.3.1_update_release_20170411_2.apk'
    no_reset = True

    try:
        opts, args = getopt.getopt(argv, 'hd:a:r:', ['devices=', 'apk=', 'reset='])
    except getopt.GetoptError:
        print 'run_tests -d <device_name> -a <apk_name> -r <reset_mode>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'run_tests -d <device_name> -a <apk_name> -r <reset_mode>'
            sys.exit()
        elif opt in ('-d', '--devices='):
            device_name = arg
        elif opt in ('-a', '--apk='):
            apk_name = arg
        elif opt in ('-r', '--reset='):
            no_reset = str2bool(arg)

    print'DEVICES_NAME=' + device_name
    print'APK_NAME=' + apk_name
    print'NO_RESET=' + str(no_reset)

    # config = WebDriverConfig()
    cp = configparser.ConfigParser()
    # print 'CURRENT_PATH=' + os.path.abspath('./settings.conf')
    file_path = os.path.abspath('./settings.conf')
    cp.read(file_path)
    cp.set('devices', 'deviceName', device_name)
    cp.set('devices', 'apkName', apk_name)
    cp.set('devices', 'noReset', str(no_reset))
    try:
        cp.write(open(file_path, 'w'))
    except IOError:
        print 'Ops, writing file failed!'

    str_time = datetime.datetime.now().strftime('%m_%d_%y_%H_%M_%S')
    results_dir = 'results/' + datetime.datetime.now().strftime('%m_%d_%y')
    if not os.path.exists(results_dir):
        os.mkdir(results_dir + '/')

    fp = file(results_dir + '/api_test_report_' + str_time + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Appium_Test_Report',
        description='This the Appium test report output by HTMLTestRunner.',
        verbosity=2
    )
    runner.run(discover)

    # # 普通报告输出
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)


if __name__ == '__main__':
    main(sys.argv[1:])
