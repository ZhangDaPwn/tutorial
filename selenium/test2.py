#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/13 11:56
# @Author   : dapwn
# @File     : test2.py
# @Software : PyCharm
# 修改input value 值方法一：
# input_button = self.driver.find_element_by_class_name("q_number")
# input_button.send_keys(Keys.CONTROL + 'a')  # 全选
# input_button.send_keys(Keys.DELETE)  # 删除，清空
# input_button.send_keys(str(num))  # 写入新的值

# 方法二：
# js = "document.getElementsByClassName('q_number')[0].value='{}';".format(str(num))
#
# self.driver.execute_script(js)
