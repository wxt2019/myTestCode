# -*- coding:UTF8—*-
from homework.class5 import Person


class Man(Person):
    name = 'tom'

    def __init__(self, n):
        Man.__init__(self)
        print('person构造函数' + n)
