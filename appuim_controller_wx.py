#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: wang
# Date: 19/03/14 15:31
# APP 微信登陆获取朋友圈


from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import time

PLATFORM = 'Android'
DEVICE_NAME = "gemini"
APP_PACKAGE = "com.tencent.mm"
APP_ACTIVITY = ".ui.LauncherUI"
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 300
MONGO_URL = "localhost"
MONGO_DB = "moments"
MONGO_COLLECTION = "moments"
USER_NAME = '13636311334'
USER_PASSWORD = '24tidy.com'


class Monments():
    def __init__(self):
        self.desired_caps = {
            "platformName": PLATFORM,
            "deviceName": DEVICE_NAME,
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def always_allow(self, number=5):
        """
        fuction:权限弹窗-始终允许
        args:1.传driver
        2.number，判断弹窗次数，默认给5次
        其它：
        WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
        :param number:
        :return:
        """
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def login(self):
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/e4g')))
        login.click()
        # 输入手机号
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/kh')))
        phone.set_text(USER_NAME)
        # 下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/axt')))
        next.click()
        # 输入密码
        password = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")))
        time.sleep(10)
        password.set_text(USER_PASSWORD)
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/axt")))
        submit.click()

    def always_not_allow(self, number=5):
        """
        fuction:权限弹窗-始终允许
        args:1.传driver
        2.number，判断弹窗次数，默认给5次
        其它：
        WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
        :param number:
        :return:
        """
        for i in range(number):
            loc = ("xpath", "//*[@text='否']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def enter(self):
        # 选项卡
        tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@text='发现']")))
        # tab = self.wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@resource-id='com.tencent.mm:id/d7_'][3]")))
        tab.click()
        moments = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/aki')))
        moments.click()


if __name__ == '__main__':
    moment = Monments()
    moment.always_allow()
    moment.login()
    moment.always_not_allow()
    moment.enter()
