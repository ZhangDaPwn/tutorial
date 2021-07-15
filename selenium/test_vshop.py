#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/13 9:48
# @Author   : dapwn
# @File     : test_vshop.py
# @Software : PyCharm
import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains


class VShopTest(object):
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

    def step_1(self, url):
        print("第一步，打开目标网站")
        self.driver.get(url)

    def step_2(self, currency):
        print("第二步，选择货币单位")
        try:
            ele_currency = self.driver.find_element_by_class_name('currency')
            ActionChains(self.driver).move_to_element(ele_currency).perform()  # 移动鼠标并悬停
            target = self.driver.find_element_by_xpath('//li[@currencyid="{}"]'.format(currency))  # 目标货币单位
            target.click()  # 点击
            time.sleep(2)
        except:
            pass

    def step_3(self, product):
        print("第三步，搜索目标商品")
        input_box = self.driver.find_element_by_id('search')  # 找到输入框
        input_box.clear()  # 清空输入框
        input_box.send_keys(product)  # 输入
        # input_box.send_keys(Keys.RETURN)  # 回车搜索,该网站不可使用回车搜索，请使用点击搜索
        submit_button = self.driver.find_element_by_id('searchSubmit')  # 搜索按钮
        submit_button.click()  # 点击
        time.sleep(2)

    def step_4(self):
        print("第四步，进入商品详情页")
        ele = self.driver.find_element_by_class_name("product-item")
        ele.click()
        time.sleep(2)

    def step_5(self, num, method):
        print("第五步，随机选择商品属性，和数量")
        if num < 1:
            num = 1
        if num > 99:
            num = 99
        self.scroll_to_bottom()  # 滑动到页面底部

        try:
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
            time.sleep(3)
        except Exception as e:
            print(e)

    def step_6(self):
        print("第六步，点击加购商品")
        self.driver.find_element_by_xpath('//i[@class="addToCart"]').click()
        time.sleep(10)

    def step_7(self):
        print("第七步，点击支付按钮")
        self.driver.switch_to.frame(0)  # 切换到当前frame
        self.scroll_to_bottom()
        eles = self.driver.find_elements_by_xpath('//div[@role="button"]')
        eles[0].click()
        time.sleep(10)

    def step_8(self):
        print("第八步，进行支付操作，页面出现故障，暂停操作")
        pass

    def main(self, url, currency, product, num, method):
        try:
            self.step_1(url)
            self.step_2(currency)
            self.step_3(product)
            self.step_4()
            self.step_5(num, method)
            self.step_6()
            self.step_7()
            self.step_8()
        except Exception as e:
            print(e)

        self.driver.close()


if __name__ == '__main__':
    vshop = VShopTest()
    url = 'http://weijiao.phigogroup.com/'
    currency = 'AUD'
    product = 'Tshirt'
    quantity_num = 20
    method = 'click'

    vshop.main(url=url, currency=currency, product=product, num=quantity_num, method=method)
