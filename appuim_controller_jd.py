#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: wang
# Date: 19/03/20 10:40

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

PLATFORM = 'Android'
DEVICE_NAME = "MI_NOTE_Pro"
APP_PACKAGE = "com.jingdong.app.mall"
APP_ACTIVITY = "main.MainActivity"
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 300
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700


class Action():
    def __init__(self):
        # 驱动
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

    def other_action(self):
        """
        允许软件请求
        :return:
        """
        try:
            e = self.wait.until(EC.presence_of_element_located((By.ID, "com.jingdong.app.mall:id/bpe")))
            e.click()
        except:
            pass

    def close_advert(self):
        """
        关闭广告
        :return:
        """
        try:
            e = self.wait.until(EC.presence_of_element_located((By.ID, "com.jingdong.app.mall:id/lz")))
            e.click()
        except:
            pass

    def always_allow(self, number=2):
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
            try:
                e = self.wait.until(EC.presence_of_element_located((By.ID, "android:id/button1")))
                e.click()
            except:
                pass

    def comments(self):
        """
        打开搜索
        点击搜索
        打开任意一个商品
        点击评价
        :return:
        """
        search = self.wait.until(EC.presence_of_element_located((By.ID, "com.jingdong.app.mall:id/a4t")))
        search.click()
        TouchAction(self.driver).tap(x=1013, y=137).perform()
        goods = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'com.jd.lib.search:id/product_list_item')))
        goods.click()
        TouchAction(self.driver).press(x=688, y=1705).move_to(x=694, y=1447).release().perform()
        # self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
        comment = self.wait.until(EC.presence_of_element_located((By.ID, "com.jd.lib.productdetail:id/pd_tab3")))
        comment.click()

    def scroll(self):
        while True:
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(10)

    def first(self):
        self.other_action()
        self.always_allow()
        self.close_advert()

    def main(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    print("开始")
    action.first()
    print("进入")
    action.main()
    print("结束")
