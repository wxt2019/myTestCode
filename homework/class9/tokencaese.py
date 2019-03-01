# -*- coding:UTF8 —*-
import requests, json

session = requests.session()
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)
token = json.loads(sessionRes.text)['token']
print(token)

# 空token
session.headers['token'] = ''
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)

# 一位token
session.headers['token'] = 'a'
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)

# token过长
session.headers['token'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)

# 未授权tokens
session.headers['token'] = '04899e6ba916448ea8e91a494fabfa81'
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)
token = json.loads(sessionRes.text)['token']

# token已授权并未登录
session.headers['token'] = token
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)
# 登录
sessionRes = session.post("http://112.74.191.10/inter/HTTP/login", data={'username': 'gulu', 'password': '123456'})
print(sessionRes.text)
# token已登录
sessionRes = session.post("http://112.74.191.10/inter/HTTP/auth")
print(sessionRes.text)
# 注销
session.post("http://112.74.191.10/inter/HTTP/logout")
