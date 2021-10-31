from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    提供公共方法的封装，即把和页面逻辑无关的方法封装在这里
    如，driver的初始化
    """

    # 添加base_url，可灵活配置测试用例的起始页
    # 可使BasePage类完全与业务逻辑解耦
    base_url = ""

    def __init__(self, base_driver = None):
        if base_driver is None:
            # 通过remote复用浏览器
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = "127.0.0.1:9222"
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            # self.driver = webdriver.Chrome()

            # # 火狐浏览器
            # Firefox_arg = webdriver.FirefoxOptions()
            # Firefox_arg.debugger_address = "127.0.0.1:7055"
            # self.driver = webdriver.Firefox(options=Firefox_arg)
            # self.driver = webdriver.Firefox()

            # 打开首页
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get(self.base_url)
            sleep(8)
            self.driver.implicitly_wait(3)
        else:
            # 给self.driver添加一个WebDriver对象注解，解决类型提示问题
            # 注解本身没有任何赋值作用，只是方便IDE操作
            self.driver: WebDriver = base_driver


    # 对页面的样板代码做个封装
    def find(self, by, locator = None):
        if locator is None:  # 只传入一个元组的情景
            return self.driver.find_element(*by)
        else:  # 传入参数等其他的情景
            return self.driver.find_element(by=by, value=locator)