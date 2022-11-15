#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random
import time
import cv2
import pyautogui
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class HandleCaptcha(object):
    def __init__(self):
        self.driver = self.start_driver()
        self.user = '【email@qq.com】'
        self.password = '【password】'
        self.username = '【username】'
        self.login_url = 'https://fxg.jinritemai.com/login'

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
        driver = Chrome('./chromedriver', options=chrome_options)
        return driver

    def sign_in(self):
        try:
            self.driver.get(self.login_url)
            time.sleep(5)
            self.driver.find_element_by_xpath('//div[text()="邮箱登录"]').click()
            time.sleep(random.uniform(2, 4))
            self.driver.find_element_by_xpath('//input[@title="邮箱"]').send_keys(self.user)
            self.driver.find_element_by_xpath('//input[@title="密码"]').send_keys(self.password)
            time.sleep(random.uniform(2, 4))
            self.driver.find_element_by_xpath('//button[text()="登录"]').click()
            time.sleep(random.uniform(2, 4))
            self.slider_verify()
            print('sign in success')
        except Exception as error:
            print('输入账密出错', error)

    def slider_verify(self):
        # 根据偏移量和手动操作模拟计算移动轨迹
        print('slider_verify')
        try_verify = 0
        SigninPage = self.driver.current_url
        while not self.check_login():
            try:
                time.sleep(random.uniform(4, 6))
                CurrentPage = self.driver.current_url
                if SigninPage != CurrentPage:
                    print("slider verify success")
                    time.sleep(5)
                    break
                # 获取背景图片元素
                target = self.driver.find_element_by_xpath('//img[@id="captcha-verify-image"]')
                # 获取滑块图片元素
                template = self.driver.find_element_by_xpath(
                    '//*[@id="sdk-login-box-slide-container"]/div/div[2]/img[2]')
                image_background = target.get_attribute('src')  # 获取背景元素下载路径
                image_slider = template.get_attribute('src')  # 获取滑块元素下载路径
                # request请求图片路径保存为二进制格式，并将其存为图片保存到本地
                res_background = requests.get(image_background)
                tth_background = res_background.content
                with open('./background.png', 'wb')as f:
                    f.write(tth_background)
                res_slider = requests.get(image_slider)
                tth_slider = res_slider.content
                with open('./slider.png', 'wb')as f:
                    f.write(tth_slider)
                print('pic download success !')
                time.sleep(random.uniform(2, 4))
            except Exception as error:
                print("储存图片出错", error)
                pass
            # 通过open-cv计算背景片偏移量
            distance = self.find_pic()
            # calculate the scale
            img = cv2.imread('./background.png')  # imread函数有两个参数，第一个参数是图片路径，第二个参数表示读取图片的形式
            # 获取实际页面上背景图片的长度
            w1 = img.shape[1]
            w2 = target.size['width']
            # 本地的图片尺寸和网页的尺寸计算出缩放比例，再把原本计算出的偏移进一步计算就可以得出网页上的偏移距离
            distance = distance * w2 / w1
            distance = int(distance)
            print('distance:{} ,{} times to try'.format(distance, try_verify + 1))
            self.slide_by_pyautogui(x=820, y=677, offset=distance)  # 滑块的坐标与实际偏移量
            return True

    def slide_by_pyautogui(self, x, y, offset):
        """
        slide by pyautogui
        :param x: X轴起始位置
        :param y: Y轴起始位置
        :param offset: 实际移动距离
        """
        # 人工智能拟人滑动算法,结合Opencv的成功率，目前有80%的成功率
        xx = x + offset
        pyautogui.moveTo(x, y, duration=2.3)
        pyautogui.mouseDown()
        y += random.randint(9, 19)
        pyautogui.moveTo(x + int(offset * random.randint(15, 23) / 20), y, duration=2.4)
        y += random.randint(-9, 0)
        pyautogui.moveTo(x + int(offset * random.randint(17, 21) / 20), y, duration=(random.randint(20, 31)) / 100)
        pyautogui.moveTo(xx, y, duration=1.8)
        pyautogui.mouseUp()

    def find_pic(self, target='./background.png', template='./slider.png'):
        try:
            # 比较图片以找出距离
            # 读取背景图片
            target_rgb = cv2.imread(target)
            # 灰度处理
            target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
            # 读取滑块图片
            template_rgb = cv2.imread(template, 0)
            # 比较位置
            res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
            # 获得结果
            distance = cv2.minMaxLoc(res)
            return distance[2][0]
        except Exception as error:
            print('破解函数出错')
            print(error)

    def check_login(self):
        if self.username in str(self.driver.page_source):
            return True
        else:
            return False

    def run_start(self):
        try:
            self.sign_in()
            time.sleep(10)
        except Exception as error:
            print(error)
        finally:
            self.driver.close()


if __name__ == '__main__':
    Crawl = HandleCaptcha()
    Crawl.run_start()
