# 0.Selenium简介

## 快速浏览

Selenium 不仅仅是一个工具或 API, 它还包含许多工具.所以Selenium更确切的描述是一个工具集，主要包含WebDriver、Selenium IDE、Grid

#### WebDriver

​		WebDriver使用浏览器供应商提供的浏览器自动化 API 来控制浏览器和运行测试. 这就像真正的用户正在操作浏览器一样. 由于 WebDriver 不要求使用应用程序代码编译其 API, 因此它本质上不具有侵入性. 因此, 您测试的应用程序与实时推送的应用程序相同.

​		其实说白了WebDriver 就是一个浏览器的驱动器，不同浏览器对应不同驱动器，**Chrome：**chromedriver  **Firefox：**FireFoxDriver **IE：**InternetExplorerDriver 等等，其中WebDriver 实现了FireFoxDriver 的驱动功能，不需要另外下载，其他浏览器需要对应下载对应版本的驱动。其中有一款特殊的浏览器：**PhantomJS（UI界面的浏览器）**，它的所有网页操作通过javascript实现，有点是加载渲染网页的速度奇快，网页的状态可以通过截屏获取，非常适合做自动化，但是17年4月核心开发人员退出项目，此后该项目不做维护了，现在基本上不适用了。

#### Selenium IDE

Selenium IDE(Integrated Development Environment 集成开发环境) 是用来开发 Selenium 测试用例的工具. 这是一个易于使用的 Chrome 和 Firefox 浏览器扩展, 通常是开发测试用例最有效率的方式. 它使用现有的 Selenium 命令记录用户在浏览器中的操作, 参数由元素的上下文确定. 这不仅节省了开发时间, 而且是学习 Selenium 脚本语法的一种很好的方法.

#### Grid

Selenium Grid允许您在不同平台的不同机器上运行测试用例. 可以本地控制测试用例的操作, 当测试用例被触发时, 它们由远端自动执行.

当开发完WebDriver测试之后, 您可能需要在多个浏览器和操作系统的组合上运行测试. 这就是 *[Grid](https://www.selenium.dev/documentation/zh-cn/grid/)* 的用途所在



# 1. 安装

## 1.1. 安装

Selenium Python bindings 提供了一个简单的API，让你使用Selenium WebDriver来编写功能/校验测试。 通过Selenium Python的API，你可以非常直观的使用Selenium WebDriver的所有功能。

Selenium Python bindings 使用非常简洁方便的API让你去使用像Firefox, IE, Chrome, Remote等等 这样的Selenium WebDrivers（Selenium web驱动器）。当前支持的版本为 2.7, 3.2及以上。

本文的用来讲解说明Selenium 2 WebDriver的API，此文档不包含Selenium 1 / Selenium RC的文档。

## 1.2. 下载 Python bindings for Selenium

可以从PyPI的官方库中下载该selenium支持库， [点此下载](https://pypi.python.org/pypi/selenium) 当然， 更好的方法当然是使用 [pip](https://pip.pypa.io/en/latest/installing/) 命令来安装selenium包。 Python3.5的 [`](https://selenium-python-zh.readthedocs.io/en/latest/installation.html#id4)标准库 <https://docs.python.org/3.5/installing/index.html>`_中包含pip命令。 使用 [`](https://selenium-python-zh.readthedocs.io/en/latest/installation.html#id6)pip`命令,你可以像下面这样安装 selenium:

```
pip install selenium
```

Note

使用Python2.x版本的用户可以手动安装pip或者easy_install，下面是easy_install 的安装方法:

easy_install selenium

你可以考虑使用`virtualenv <[http://www.virtualenv.org](http://www.virtualenv.org/)>`_ 创建独立的Python环境。Python3.5中`pyvenv <https://docs.python.org/3.5/using/scripts.html#scripts-pyvenv>`_ 可以提供几乎一样的功能。

## 1.3. Windows用户的详细说明

Note

请在有网的情况下执行该安装命令。

1. 安装Python3.5：[官方下载页](http://www.python.org/download).

2. 从开始菜单点击运行（或者`Windows+R`）输入`cmd`,然后执行下列命令安装:

   ```
   C:\Python35\Scripts\pip.exe install selenium
   ```

现在你可以使用Python运行测试脚本了。 例如：如果你创建了一个selenium的基本示例并且保存在了``C:my_selenium_script.py``，你可以如下执行:

```
C:\Python35\python.exe C:\my_selenium_script.py
```

## 1.4. 下载 Selenium 服务器

Note

如果你想使用一个远程的WebDriver，Selenium服务是唯一的依赖， 参见 [使用远程 Selenium WebDriver](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html#selenium-remote-webdriver) 获得更多细节。 如果你只是刚刚开始学习使用Selenium，你可以忽略该章节直接开始下一节。

Selenium server是一个JAVA工程，Java Runtime Environment (JRE) 1.6或者更高的版本是推荐的运行环境。

你可以在 [该下载页](http://seleniumhq.org/download/) 下载2.x的Selenium server，这个文件大概长成这个样子：`selenium-server-standalone-2.x.x.jar`， 你可以去下载最新版本的2.x server。

如果你还没有安装Java Runtime Environment (JRE)的话， 呢，[在这下载](http://www.oracle.com/technetwork/java/javase/downloads/index.html)， 如果你是有的是GNU/Linux系统，并且巧了，你还有root权限，你还可以使用操作系统指令去安装JRE。

如果你把`java`命令放在了PATH(环境变量)中的话，使用下面命令安装:

```
java -jar selenium-server-standalone-2.x.x.jar
```

当然了，把``2.x.x``换成你下载的实际版本就可以了。

如果是不是root用户你或者没有把JAVA放到PATH中， 你可以使用绝对路径或者相对路径的方式来使用命令， 这个命令大概长这样子:

```
/path/to/java -jar /path/to/selenium-server-standalone-2.x.x.jar
```



# 2. 快速入门

## 2.1. 简单用例

如果你已经安装好了selenium，你可以把下面的python代码拷贝到你的编辑器中

```python
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
```

上面的脚本可以保存到一个文件（如：- test0.py），那么可以这样使用

```python
python test0.py
```

你运行的 python 环境中应该已经安装了 selenium 模块。

## 2.2. 示例详解

selenium.webdriver 模块提供了所有WebDriver的实现， 当前支持的WebDriver有： Firefox, Chrome, IE and Remote。 [`](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html#id4)Keys`类提供键盘按键的支持，比如：RETURN, F1, ALT等

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

接下来，创建一个Chrome WebDriver的实例

```python
driver = webdriver.Chrome()
```

driver.get 方法将打开URL中填写的地址，WebDriver 将等待， 直到页面完全加载完毕（其实是等到”onload” 方法执行完毕），然后返回继续执行你的脚本。 值得注意的是，如果你的页面使用了大量的Ajax加载， WebDriver可能不知道什么时候页面已经完全加载:

```
driver.get("http://www.python.org")
```

下一行是用assert的方式确认标题是否包含“Python”一词。 (译注：assert 语句将会在之后的语句返回false后抛出异常，详细内容可以自行百度)

```
assert "Python" in driver.title
```

WebDriver 提供了大量的方法让你去查询页面中的元素，这些方法形如： find_element_by_*。 例如：包含 name 属性的input输入框可以通过 find_element_by_name 方法查找到， 详细的查找方法可以在第四节元素查找中查看:

```python
elem = driver.find_element_by_name("q")
```

接下来，我们发送了一个关键字，这个方法的作用类似于你用键盘输入关键字。 特殊的按键可以使用Keys类来输入，该类继承自 selenium.webdriver.common.keys， 为了安全起见，我们先清除input输入框中的任何预填充的文本（例如：”Search”）,从而避免我们的搜索结果受影响：

```python
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面后,你会得到所有的结果。为了确保某些特定的结果被找到，使用`assert`如下:

```
assert "No results found." not in driver.page_source
```

最后，关闭浏览器窗口，你还可以使用quit方法代替close方法， quit将关闭整个浏览器，而_close——只会关闭一个标签页， 如果你只打开了一个标签页，大多数浏览器的默认行为是关闭浏览器:

```
driver.close()
```

## 2.3. 用Selenium写测试用例

Selenium 通常被用来写一些测试用例. selenium 包本身不提供测试工具或者框架. 你可以使用Python自带的模块unittest写测试用例。 The other options for a tool/framework are py.test and nose.

在本章中，我们使用 unittest 来编写测试代码，下面是一个已经写好的用例。 这是一个在 python.org 站点上搜索的案例:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

你可以在shell中运行下列代码:

```python
python test_python_org_search.py
.
----------------------------------------------------------------------
Ran 1 test in 15.566s

OK
```

结果表明这个测试用例已经成功运行。

## 2.4. 逐步解释测试代码

一开始，我们引入了需要的模块， [unittest](http://docs.python.org/library/unittest.html) 模块是基于JAVA JUnit的Python内置的模块。 该模块提供了一个框架去组织测试用例。 selenium.webdriver 模块提供了所有WebDriver的实现。 现在支持的WebDriver有：Firefox, Chrome, IE and Remote. Keys 类提供所有的键盘按键操作，比如像这样的：

> RETURN, F1, ALT等。

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

该测试类继承自 unittest.TestCase. 继承 TestCase 类是告诉 unittest 模块该类是一个测试用例:

```python
class PythonOrgSearch(unittest.TestCase):
```

setUp 方法是初始化的一部分, 该方法会在该测试类中的每一个测试方法被执行前都执行一遍。 下面创建了一个Firefox WebDriver的一个实例。

```python
def setUp(self):
    self.driver = webdriver.Firefox()
```

这是一个测试用例实际的测试方法. 测试方法始终以 test`开头。 在该方法中的第一行创建了一个在 `setUp 方法中创建的驱动程序对象的本地引用。

```python
def test_search_in_python_org(self):
    driver = self.driver
```

driver.get 方法将会根据方法中给出的URL地址打开该网站。 WebDriver 会等待整个页面加载完成（其实是等待”onload”事件执行完毕）之后把控制权交给测试程序。 如果你的页面使用大量的AJAX技术来加载页面，WebDriver可能不知道什么时候页面已经加载完成:

```python
driver.get("http://www.python.org")
```

下面一行使用assert断言的方法判断在页面标题中是否包含 “Python”

```python
self.assertIn("Python", driver.title)
```

WebDriver 提供很多方法去查找页面值的元素，这些方法都以 find_element_by_* 开头。 例如：包含 name 属性的input元素可以使用

> find_element_by_name`方法查找到。详细的细节可以参照 :ref:`locating-elements 章节:
>
> ```python
> elem = driver.find_element_by_name("q")
> ```
>
> 

接下来我们发送keys，这个和使用键盘输入keys类似。 特殊的按键可以通过引入`selenium.webdriver.common.keys`的 Keys 类来输入

```python
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面之后，无论如何你都会得到搜索结果，为了确保某些结果类检索到，可以使用下列断言 After submission of the page, you should get result as per search if

```python
assert "No results found." not in driver.page_source
```

tearDown 方法会在每一个测试方法执行之后被执行。 该方法可以用来做一些清扫工作，比如关闭浏览器。 当然你也可以调用 quit 方法代替`close`方法，

> quit 将关闭整个浏览器，而`close`只会关闭一个标签页， 如果你只打开了一个标签页，大多数浏览器的默认行为是关闭浏览器。

```python
def tearDown(self):
    self.driver.close()
```

下面是入口函数:

```python
if __name__ == "__main__":
    unittest.main()
```



# 3. 打开一个页面

你想做的第一件事也许是使用WebDriver打开一个链接。 常规的方法是调用 `get` 方法:

```python
driver.get("http://www.google.com")
```

WebDriver 将等待，直到页面完全加载完毕（其实是等到 `onload` 方法执行完毕）， 然后返回继续执行你的脚本。 值得注意的是，如果你的页面使用了大量的Ajax加载， WebDriver可能不知道什么时候页面已经完全加载。 如果你想确保也main完全加载完毕，可以使用:ref:waits <waits>

## 3.1. 与页面交互

只是打开页面其实并没有什么卵用。我们真正想要的是与页面做交互。 更具体地说，对于一个页面中的HTML元素，首先我们要找到他。WebDriver 提供了大量的方法帮助你去查找元素，例如：已知一个元素定义如下:

```
<input type="text" name="passwd" id="passwd-id" />
```

你可以通过下面的方法查找他:

```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```

你还可以通过链接的文本查找他，需要注意的是，这个文本必须完全匹地配。 当你使用`XPATH`时，你必须注意，如果匹配超过一个元素，只返回第一个元素。 如果上面也没找到，将会抛出 [``](https://selenium-python-zh.readthedocs.io/en/latest/navigating.html#id3)NoSuchElementException``异常。

WebDriver有一个”基于对象”的API; 我们使用相同的接口表示所有类型的元素。 这就意味着，当你打开你的IDE的自动补全的时候，你会有很多可以调用的方法。 但是并不是所有的方法都是有意义或是有效的。不过不要担心！ 当你调用一些毫无意义的方法时，WebDriver会尝试去做一些正确的事情（例如你对一个”meta” 元素调用”setSelected()”方法的时候）。

所以，当你拿到ige元素时，你能做什么呢？首先，你可能会想在文本框中输入一些内容:

```
element.send_keys("some text")
```

你还可以通过”Keys”类来模拟输入方向键:

```
element.send_keys(" and some", Keys.ARROW_DOWN)
```

对于任何元素，他可能都叫 send_keys ，这就使得它可以测试键盘快捷键， 比如当你使用Gmail的时候。但是有一个副作用是当你输入一些文本时，这些 输入框中原有的文本不会被自动清除掉，相反，你的输入会继续添加到已存在文本之后。 你可以很方便的使用 clear 方法去清除input或者textarea元素中的内容:

```
element.clear()
```

## 3.2. 填写表格

我们已经知道如何在input或textarea元素中输入内容，但是其他元素怎么办？ 你可以“切换”下拉框的状态，你可以使用``setSelected``方法去做一些事情，比如 选择下拉列表，处理`SELECT`元素其实没有那么麻烦:

```
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
```

上面这段代码将会寻找页面第一个 “SELECT” 元素, 并且循环他的每一个OPTION元素， 打印从utamen的值，然后按顺序都选中一遍。

正如你说看到的那样，这不是处理 SELECT 元素最好的方法。WebDriver的支持类包括一个叫做 [``](https://selenium-python-zh.readthedocs.io/en/latest/navigating.html#id6)Select``的类，他提供有用的方法处理这些内容:

```
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

WebDriver 也提供一些有用的方法来取消选择已经选择的元素:

```
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

这将取消选择所以的OPTION。

假设在一个案例中，我们需要列出所有已经选择的选项，Select类提供了方便的方法来实现这一点:

```
select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options
```

获得所以选项:

```
options = select.options
```

一旦你填写完整个表单，你应该想去提交它，有一个方法就是去找到一个“submit” 按钮然后点击它:

```
# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()
```

或者，WebDriver对每一个元素都有一个叫做 “submit” 的方法，如果你在一个表单内的 元素上使用该方法，WebDriver会在DOM树上就近找到最近的表单，返回提交它。 如果调用的元素不再表单内，将会抛出``NoSuchElementException``异常:

```
element.submit()
```

## 3.3. 拖放

您可以使用拖放，无论是移动一个元素，或放到另一个元素内:

```
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```

## 3.4. 在不同的窗口和框架之间移动

对于现在的web应用来说，没有任何frames或者只包含一个window窗口是比较罕见的。 WebDriver 支持在不同的窗口之间移动，只需要调用``switch_to_window``方法即可:

```
driver.switch_to_window("windowName")
```

所有的 `driver` 将会指向当前窗口，但是你怎么知道当前窗口的名字呢，查看打开他的javascript或者连接代码:

```
<a href="somewhere.html" target="windowName">Click here to open a new window</a>
```

或者，你可以在”switch_to_window()”中使用”窗口句柄”来打开它， 知道了这些，你就可以迭代所有已经打开的窗口了:

```
for handle in driver.window_handles:
    driver.switch_to_window(handle)
```

你还可以在不同的frame中切换 (or into iframes):

```
driver.switch_to_frame("frameName")
```

通过“.”操作符你还可以获得子frame，并通过下标指定任意frame，就像这样:

```
driver.switch_to_frame("frameName.0.child")
```

如何获取名叫“frameName”的frame中名叫 “child”的子frame呢？ **来自\*top\*frame的所有的frame都会被评估** （**All frames are evaluated as if from \*top\*.**）

一旦我们完成了frame中的工作，我们可以这样返回父frame:

```
driver.switch_to_default_content()
```

## 3.5. 弹出对话框

Selenium WebDriver 内置了对处理弹出对话框的支持。 在你的某些动作之后可能会触发弹出对话框，你可以像下面这样访问对话框:

```
alert = driver.switch_to_alert()
```

它将返回当前打开的对话框对象。使用此对象，您现在可以接受、排除、读取其内容， 甚至可以在prompt对话框中输入(译注：prompt()是对话框的一种，不同于alert()对话框，不同点可以自行百度)。 这个接口对alert, confirm， prompt 对话框效果相同。 参考相关的API文档获取更多信息。

## 3.6. 访问浏览器历史记录

在之前的文章中，我们使用``get``命令打开一个页面, ( `driver.get("http://www.example.com")`)，WebDriver有很多更小的，以任务为导向的接口， navigation就是一个有用的任务，打开一个页面你可以使用`get`:

```
driver.get("http://www.example.com")
```

在浏览历史中前进和后退你可以使用:

```
driver.forward()
driver.back()
```

请注意，这个功能完全取决于底层驱动程序。当你调用这些方法的时候，很有可能会发生意想不到的事情， 如果你习惯了浏览器的这些行为于其他的不同。（原文：It’s just possible that something unexpected may happen when you call these methods if you’re used to the behaviour of one browser over another.）

## 3.7. 操作Cookies

在我们结束这一节之前，或许你对如何操作Cookies可能会很感兴趣。 首先，你需要打开一个也面，因为Cookie是在某个域名下才生效的:

```
::
```

> \# 打开一个页面 driver.get(“[http://www.example.com](http://www.example.com/)”)
>
> \# 现在设置Cookies，这个cookie在域名根目录下（”/”）生效 cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’} driver.add_cookie(cookie)
>
> \# 现在获取所有当前URL下可获得的Cookies driver.get_cookies()





















































sdkjfkljsldk;jfakl;ll;akfj