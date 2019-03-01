from selenium import webdriver
import os, traceback

def getchrome():
    # 调用chrome浏览器
    # 去掉浏览器顶部提示条
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 为提高浏览的速度，获取用户的用户目录
    try:
        # 获取到userdir路径
        userdir =os.environ['USERPROFILE']
    except Exception as e:
        # 打印错误信息提示
        traceback.print_exc()
        # 没有获取到userdir路径，使用默认值
        userdir = 'C:\\Users\\MECHREVO'
    # 追加固定的地址,获取用户目录的全路径
    userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
    userdir = 'user-data-dir' + userdir
    # 添加用户目录（!运行时不能运行Chrome浏览器）
    option.add_argument(userdir)
    # 创建对象driver浏览器对象
    chromedriver = webdriver.Chrome(executable_path='../lib/chromedriver', options=option)
    # 浏览器浏览URL地址
    # chromedriver.get('http://112.74.191.10:8000/')
    return chromedriver

def getFirefox():
    geckodriver = webdriver.Firefox(executable_path='../lib/geckodriver')
    return geckodriver

def getIe():
    iedriver = webdriver.Ie(executable_path='../lib/IEDriverServer')
    iedriver.get('https://www.baidu.com')
    return iedriver



