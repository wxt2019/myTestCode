import requests, json

session = requests.session()
session.headers['token'] = ''
# token授权
sessionreuslt = session.post("http://112.74.191.10/inter/HTTP/auth")
result = json.loads(sessionreuslt.text)
print(result)
token = result['token']
print(token)

session.headers['token'] = token
sessionreuslt = session.post('http://112.74.191.10/inter/HTTP/register',
                             data={'username': 'we22', 'password': '123456', 'nickname': '12443', 'describe': ''})
result = json.loads(sessionreuslt.text)
print(result)
