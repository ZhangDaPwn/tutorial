import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # 使用webdriver启动Chrome浏览器
driver.get("http://www.python.org")  # 访问目标网站
title = driver.title  # 获取目标网站标题
print("网页标题为：", title)  # 打印结果
elem = driver.find_element_by_name("q")  # 使用name属性进行元素定位
elem.clear()  # 清空输入框中的内容
elem.send_keys("pycon")  # 输入自己定义内容至输入框中
elem.send_keys(Keys.RETURN)  # 按下回车键，进行搜索
time.sleep(8)  # 停留8秒用来展示
driver.close()  # 关闭浏览器
