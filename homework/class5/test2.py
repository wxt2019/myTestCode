# -*- coding:UTF8 -*-

from homework.class5.Person import Person, Man, Woman

print("**************调用实例变量/函数**************")
# peron1 = Person()
#
# # 调用实例变量
# peron1.food = '西瓜'
# # 调用实力方法
# peron1.eat('小明')
# print("**************调用类变量/函数**************")
# # 调用类变量
# print(Person.type)
# Person.maketools()

print("**************man继承变量/函数**************")
man1 = Man(2)
man1.run()
print(man1.type)
# 调用自己类的变量和方法
man1.name = 'john'
man1.car()

print("**************man继承变量/函数**************")
Woman.sweater()
woman1 = Woman(1)
woman1.run()
woman1.maketools('xiaohua')
