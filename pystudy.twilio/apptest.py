# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :

from appium import webdriver


desired_caps = {

        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '4.2',
        'appPackage': 'com.android.calculator2',
        'appActivity': 'com.android.calculator2.Calculator'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_name('7').click()
driver.find_element_by_name('+').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('=').click()