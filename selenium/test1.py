import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    # 准备环境，执行每个测试用例的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_0_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_1(self):
        print("im test 1")

    def test_2(self):
        print("im test 2")

    # 环境还原，执行每个测试用例的后置条件
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # 启动单元测试
    unittest.main()  # unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z
