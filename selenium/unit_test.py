import unittest  # 测试框架
import time  # 时间包
import random
from selenium import webdriver  # 浏览器驱动
from selenium.webdriver.common.keys import Keys  # 键盘相关操作
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标相关操作


class PythonOrgSearch(unittest.TestCase):

    # 准备环境，执行每个测试用例的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # 访问python.org网站，打印标题
    def test_0_search_in_python_org(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)  # 断言打印
        print("打印标题：", self.driver.title)
        elem = self.driver.find_element_by_name("q")  # 到搜索框
        elem.clear()  # 清空输入框 此案例也可以不进行清空
        elem.send_keys("pycon")  # 输入
        elem.send_keys(Keys.RETURN)  # 回车搜索
        assert "No results found." not in self.driver.page_source  # 断言判断异常

    def test_1_open_page(self):
        print("打开Google网页，并截图保存")
        self.driver.get('http://www.google.com')
        self.driver.save_screenshot('google.png')
        print("该网页的标题为：", self.driver.title)
        time.sleep(5)

    def test_2_choice_address(self):
        print("打开vhsop店铺，并选择一个目标货币单位")
        currency = 'AUD'  # 澳元
        self.driver.get('http://weijiao.phigogroup.com/')
        ele_currency = self.driver.find_element_by_class_name('currency')
        ActionChains(self.driver).move_to_element(ele_currency).perform()  # 移动鼠标并悬停
        target = self.driver.find_element_by_xpath('//li[@currencyid="{}"]'.format(currency))  # 目标货币单位
        target.click()  # 点击
        time.sleep(5)

    def test_3_search(self):
        print("打开vhsop店铺，并搜索一件你的目标商品")
        self.driver.get('http://weijiao.phigogroup.com/')
        # self.driver.implicitly_wait(5)  # 隐性等待5秒
        input_box = self.driver.find_element_by_id('search')  # 找到输入框
        input_box.clear()  # 清空输入框
        input_box.send_keys('Tshirt')  # 输入
        # input_box.send_keys(Keys.RETURN)  # 回车搜索,该网站不可使用回车搜索，请使用点击搜索
        submit_button = self.driver.find_element_by_id('searchSubmit')  # 搜索按钮
        submit_button.click()  # 点击
        time.sleep(10)

    def test_4_scroll_to_bottom(self):
        print("打开简单网并滑动到页面底部")
        self.driver.get('http://jandan.net/')
        js1 = "return action=document.body.scrollHeight"
        js2 = "window.scrollTo(0, {})"
        height = self.driver.execute_script(js1)
        for i in range(0, height, 1000):
            self.driver.execute_script(js2.format(i))
            time.sleep(0.5)

    def test_5_scroll_to_target_element(self):
        print("打开简单网并滑动到目标元素")
        self.driver.get('http://jandan.net/p/109251')
        js_script = "arguments[0].scrollIntoView();"
        ele = self.driver.find_element_by_id("shang-button")
        self.driver.execute_script(js_script, ele)
        print("目标元素：", ele.text)
        time.sleep(5)

    def test_6_into_product_detail_page(self):
        print("点击进入目标商品详情页")
        self.driver.get('http://weijiao.phigogroup.com/productList.html?keyword=Tshirt')
        ele = self.driver.find_element_by_class_name("product-item")
        ele.click()
        time.sleep(5)

    def test_7_choice_and_add_to_cart(self):
        print("随机选择商品属性并添加如购物车")
        num = random.randint(1, 99)
        method = 'click'
        url = 'http://weijiao.phigogroup.com/productDetail_81332.html'
        self.driver.get(url)
        js1 = "return action=document.body.scrollHeight"
        js2 = "window.scrollTo(0, {})"
        height = self.driver.execute_script(js1)
        for i in range(0, height, 1000):
            self.driver.execute_script(js2.format(i))
            time.sleep(0.5)

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

    # 环境还原，执行每个测试用例的后置条件
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # 启动单元测试
    unittest.main()  # unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z
