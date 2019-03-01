from selenium import webdriver
import traceback, os, time


class web:
    # 定义实例变量
    def __init__(self):
        self.driver = None

    def webdriver(self, brower='cc', waittime=10):
        if brower == 'cc':
            # 调用chrome浏览器
            # 去掉浏览器顶部提示条
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            # 为提高浏览的速度，获取用户的用户目录
            try:
                # 获取到userdir路径
                userdir = os.environ['USERPROFILE']
            except Exception as e:
                # 打印错误信息提示
                traceback.print_exc()
                # 没有获取到userdir路径，使用默认值
                userdir = 'C:\\Users\\MECHREVO'
            # 追加固定的地址,获取用户目录的全路径
            userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
            userdir = 'user-data-dir' + userdir
            # 添加用户目录（运行时不能运行Chrome浏览器）
            option.add_argument(userdir)
            # 创建对象driver浏览器对象
            self.driver = webdriver.Chrome(executable_path='../lib/chromedriver', options=option)
            # 去掉 data;的出现
            #option
            return self.driver

        if brower == 'ff':
            self.driver = webdriver.Firefox(executable_path='../lib/geckodriver')
            return self.driver

        if brower == 'ie':
            self.driver = webdriver.Ie(executable_path='../lib/IEDriverServer')
            return self.driver


