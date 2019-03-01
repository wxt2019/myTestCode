# -*- coding:UTF8—*-
# 人类

class Person:
    # 定义变量
    colorskin = "黄皮肤"
    type = '黄种人'

    # 构造函数
    def __init__(self, n):
        # 实例变量
        # 私有变量
        self.__name = 'Tom'
        self.food = '苹果'
        print('man构造函数'+str(n))

    # 定义方法
    def eat(self, p):
        print(p+'正在吃' + self.food)

    # 调用私有变量函数
    def run(self):
        print(self.__name+'奔跑回家')
        # self.__hunting()


    # 定义类方法
    @classmethod
    def maketools(cls):
        # cls.__hunting()
        print('制造工具')

    #私有方法
    def __hunting(self):
        print(self.__name+'制造工具')


class Man(Person):
    sex = '男'

    def __init__(self, n):
        Person.__init__(self, n)
        self.name = 'tom'
        self.headcolor = '黑色'
        print('person构造函数')

    def car(self):
        print(self.name + '开车上班')


class Woman(Person):
    sex = '女人'
    name = 'susie'


    #扩展
    @classmethod
    def sweater(cls):
        print(cls.sex + '织毛衣')

    # 重写
    def run(self):
        print(self.name + '在慢跑')

    # 继承重写
    def maketools(self, n):
        print(n + '制造工具')
