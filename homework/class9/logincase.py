# -*- coding:UTF8 —*-
import requests
import json


session = requests.session()
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)
result = json.loads(sessionRes.text)

# 注销
sessionRes = session.post('http://112.74.191.10/inter/HTTP/logout')
result = json.loads(sessionRes.text)

# 无token
session.headers['token'] = ''
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
# print(result)
if result['status'] == 405:
    print('pass')

# token过长
session.headers['token'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
# print(result)
if result['status'] == 405:
    print('pass')

# token未授权
session.headers['token'] = '0d862fe621a04bca86489a554945b202'
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
# print(result)
if result['status'] == 405:
    print('pass')

# token已授权
session.headers['token'] = ''
sessionRes = session.post('http://112.74.191.10/inter/HTTP/auth')
result = json.loads(sessionRes.text)
print(result)

# 获取保存已授权token
token = result['token']
sessionRes.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 200:
    print(200)

# token已登录
session.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 406:
    print('pass')

# 注销
session.post('http://112.74.191.10/inter/HTTP/logout')

# 登录用户名为空

session.headers['token'] = ''
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
token = json.loads(sessionRes.text)['token']
# 更新token
session.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': None, 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')

# 登录无用户名
session.headers['token'] = ''
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
token = json.loads(sessionRes.text)['token']
# 更新token
session.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')

# 用户名是特殊字符串
print('特殊字符')
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': '#￥%a？', 'password': '123456'})
result = json.loads(sessionRes.text)
print(result)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': '큐〓㊚a？', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'Wil🚣l？', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 用户名边界值（3-16位）
print('用户名边界值（3-16位）')
# 用户名2位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'qa', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 用户名3位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'q2a', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 用户名16位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'qQWEQWEQWEQWEQWE', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 用户名17位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'qQQWEQWEQWEQWEQWE', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 用户名过长
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'qQQWEQWEQWEQWEQWEQWEQWEQWEQWEQW', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码边界值测试
print('密码边界值测试：3-16位')
# 无密码
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu'})
result = json.loads(sessionRes.text)
print(result)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码为空
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': ''})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码2位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '12'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码3位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 密码16位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'gulu', 'password': '1234567891234567'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 密码17位
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'gulu', 'password': '12345678912345678'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码过长
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'gulu', 'password': '1234567891234567123456789123456'})
result = json.loads(sessionRes.text)
if result['status'] == 402:
    print('pass')
else:
    print('fail')

# 密码特殊字符
print('密码特殊字符')
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '@#$@#'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 密码带表情
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login",
                          data={'username': 'gulu', 'password': 'Thanks♪(･ω･)ﾉ'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 字段测试
# 多一个字段
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'aaa':'bbb','password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')
session.post('http://112.74.191.10/inter/HTTP/logout')
# 更新token

session.headers['token'] = ''
sessionRes = session.post('http://112.74.191.10/inter/HTTP/auth')
result = json.loads(sessionRes.text)
token = result['token']

# 等价类测试
print('等价类测试')
# 用户名密码错误
session.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '11111'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 用户名不存在
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'ggggg', 'password': '11111'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')

# 用户名密码不匹配
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': 'tufei'})
result = json.loads(sessionRes.text)
if result['status'] == 401:
    print('pass')
else:
    print('fail')
# 用户名密码匹配
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
result = json.loads(sessionRes.text)
if result['status'] == 200:
    print('pass')
else:
    print('fail')

# 注销
sessionRes = session.post('http://112.74.191.10/inter/HTTP/logout')
result = json.loads(sessionRes.text)
print(result)
# 更新token
session.headers['token'] = ''
sessionRes = session.post('http://112.74.191.10/inter/HTTP/auth')
result = json.loads(sessionRes.text)
token = result['token']
session.headers['token'] = token
sessionRes = session.post('http://112.74.191.10/inter/HTTP/logout')
result = json.loads(sessionRes.text)
print(result)




