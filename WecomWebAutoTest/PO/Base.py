from selenium import webdriver

class BasePage:
    """
    提供公共方法的封装，即把和页面逻辑无关的方法封装在这里
    如，driver的初始化
    """
    def __init__(self):
        # 通过remote复用浏览器
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = "127.0.0.1:9222"
        # 实例化driver对象
        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver = webdriver.Chrome()
        # 打开首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(3)