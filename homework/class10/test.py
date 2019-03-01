# -*- coding:UTF8 —*-


from homework.class10.httpkeys import HTTP

http =HTTP()
# token 位空
http.addheaders('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token 为一位
http.addheaders('token', 'a')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token 超长
http.addheaders('token', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token 未授权
http.addheaders('token', '109f1a34bdcf4785b6c70a9917d7a49d')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')


# 保存token
http.savejson('t', 'token')
# token 已授权
http.addheaders('token', '{t}')
print(http.session.headers)
http.post('http://112.74.191.10:8081/inter/HTTP/login', 'username=root&password=123')
http.assertequals('status', '200')

http.post('http://112.74.191.10:8081/inter/HTTP/logout')

# 获取用户信息

http.addheaders('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.savejson('t', 'token')
http.addheaders('token', '{t}')
http.post('http://112.74.191.10:8081/inter/HTTP/login', 'username=gulu&password=123456')
print(http.session.headers)
http.savejson('id', 'userid')
http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo', 'id={id}')
http.assertequals('status', '200')
# 已登录注销
http.post('http://112.74.191.10:8081/inter/HTTP/logout')

# 未登录注销
http.addheaders('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.savejson('t', 'token')
http.addheaders('token', '{t}')
http.post('http://112.74.191.10:8081/inter/HTTP/logout')
http.assertequals('status', '200')

# 注册

http.addheaders('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.savejson('t', 'token')
http.addheaders('token', '{t}')
http.post('http://112.74.191.10:8081/inter/HTTP/register', 'username=gulu11&password=123456&nickname=nike&describe=')
http.assertequals('status', '200')