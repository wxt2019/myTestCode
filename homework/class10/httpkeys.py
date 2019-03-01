# -*- coding:UTF8 —*-
import requests, json


class HTTP:
    # 构造函数
    def __init__(self):
        # 初始化session变量
        self.session = requests.session()
        # 用来存放json解析结果
        self.jsonre = {}
        # 保存数据,实现关联
        self.param = {}

    # 访问url
    def post(self, url, data=None):
        if data is None:
            result = self.session.post(url)
        else:
            # 将参数替换成值, 当没有传参{}时，将不会执行
            data = self.__params(data)
            # 将字符串处理成字典
            datas = self.__todic(data)
            print(datas)
            result = self.session.post(url, data=datas)
        self.jsonre = json.loads(result.text)
        print(self.jsonre)

    # 添加头
    def addheaders(self, token, value):
        str = self.__params(value)
        print(str)
        self.session.headers[token] = str

    # 保存token
    def savejson(self, k, key):
        self.param[k] = self.jsonre[key]
        print(self.param['t'])

    # 验证
    def assertequals(self, key, value):
        if str(self.jsonre[key]) == str(value):
            print("PASS")
        else:
            print("FAIL")

    # 字符串处理，将规定模式的{t} 形式，改成对应的参数值
    def __params(self, str):

        for key in self.param:
            str = str.replace("{" + key + "}", self.param[key])
        return str

    # 处理参数字符创转化为字典
    def __todic(self, str):
        # 用来保存拆分的字典
        par = {}
        # 拆分参数
        params = str.split('&')
        for pa in params:
            ar = pa.split('=')
            par[ar[0]] = ar[1]
        return par
