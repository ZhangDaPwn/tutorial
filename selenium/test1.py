#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/13 9:48
# @Author   : dapwn
# @File     : test1.py
# @Software : PyCharm
import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions


class VShop(object):
    def __init__(self):
        self.headless = False
        self.options = ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者选项
        if self.headless:
            self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def scroll_to_bottom(self):
        js1 = "return action=document.body.scrollHeight"
        js2 = "window.scrollTo(0, {})"
        height = self.driver.execute_script(js1)
        for i in range(0, height, 1000):
            self.driver.execute_script(js2.format(i))
            time.sleep(0.5)

    def test1(self, num: int, method='input'):
        url = 'http://weijiao.phigogroup.com/productDetail_80803.html'
        if num < 1:
            num = 1
        if num > 99:
            num = 99
        self.driver.get(url)
        self.scroll_to_bottom()

        attrs = self.driver.find_elements_by_xpath('//div[@id="mlpSpe"]/div')
        # 循环随机点选参数
        for attr in attrs:
            # 参数类型一：列表
            lis = attr.find_elements_by_xpath('./ul/li')
            lis[random.randint(1, len(lis))].click()

        if method == 'click':
            add_button = self.driver.find_element_by_class_name("addBtn")
            reduce_button = self.driver.find_element_by_class_name("reduceBtn")
            for index in range(num):
                add_button.click()
                time.sleep(0.1)

            # 检查数量是否正确，若不正确，响应的增减数量
            number_element = self.driver.find_element_by_class_name("q_number")
            number = number_element.get_attribute("value")
            D_value = int(number) - num

            if D_value == 0:
                pass
            elif D_value > 0:
                for i in range(abs(D_value)):
                    reduce_button.click()
                    time.sleep(0.1)
            else:
                for i in range(abs(D_value)):
                    add_button.click()
                    time.sleep(0.1)

        else:
            js = "document.getElementsByClassName('q_number')[0].value='{}';".format(str(num))
            self.driver.execute_script(js)
            # 检查数量是否正确，若不正确，响应的增减数量
            number_element = self.driver.find_element_by_class_name("q_number")
            number = number_element.get_attribute("value")
            D_value = int(number) - num
            if D_value != 0:
                self.driver.execute_script(js)

        self.driver.find_element_by_xpath('//i[@class="addToCart"]').click()
        time.sleep(10)

        self.driver.close()


if __name__ == '__main__':
    vshop = VShop()
    quantity_num = 20
    method = 'click'
    vshop.test1(num=quantity_num, method=method)
