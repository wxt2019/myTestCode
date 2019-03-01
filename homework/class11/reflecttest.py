# -*- coding:UTF8 —*-
from homework.class10.httpkeys import HTTP
import inspect

a = ['', '', '无token', 'post', 'http://112.74.191.10:8081/inter/HTTP/auth', '', '', '']
http = HTTP()
# 获取http实例中的对应a 的方法
print(a[3])
fun = getattr(http, a[3])
print(fun)
# 获取方法的参数
aargs = inspect.getfullargspec(fun).__str__()
print(aargs)
# # 截取参数
args = aargs[aargs.find('args=')+5:aargs.find(', varargs')]
print(args)
args = eval(args)
args.remove('self')
print(args)

# 获取参数个数
ln = len(args)

if ln < 1:
    fun()

if ln < 2:
    fun(a[4])

if ln < 3:
    fun(a[4], a[5])
