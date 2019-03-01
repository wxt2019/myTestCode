from selenium import webdriver
from homework.class7 import Webdriver
import time

web = Webdriver.web()
driver = web.webdriver(brower='ff')
driver.maximize_window()
# 访问url地址
driver.get('http://112.74.191.10:8000/')
# time.sleep(5)
# driver.implicitly_wait(5)

# 登录
loginelement = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
loginelement.click()

# 输入登录数据
loginname = driver.find_element_by_id('username')
loginname.send_keys('13800138006')
pwd = driver.find_element_by_id('password')
pwd.send_keys('123456')
yzm = driver.find_element_by_id('verify_code')
yzm.send_keys('111111')
sub = driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a')
sub.click()

driver.implicitly_wait(3)
# 返回首页
bac = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/a/img').click()
driver.implicitly_wait(5)

# 输入搜索商品名称
searchele = driver.find_element_by_id('q')
searchele.send_keys('手机')

# 点击搜索按钮
but = driver.find_element_by_xpath('//*[@id="searchForm"]/button')
but.click()

# 加入购物车
shopcar = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[6]/div/div[5]/div[2]/a')
shopcar.click()

# 立即购买
# buy = driver.find_element_by_xpath('//*[@id="buy_now"]')
# buy.click()
# time.sleep(3)

# 进入iframe
# iframe = driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
# driver.switch_to.frame(iframe)
driver.switch_to.frame('layui-layer-iframe1')

driver.implicitly_wait(3)
# 定位iframe中的元素
ele = driver.find_element_by_xpath('/html/body/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div/span')
if ele.text == "添加成功":
    # 去购物车结算
    driver.find_element_by_css_selector('a.ui-button:nth-child(2)').click()
else:
    print("商品添加购物车失败！")

# 切除iframe
driver.switch_to.default_content()

# 判断购物车结算商品的数量
# shopnumele = driver.find_element_by_xpath('//*[@id="goods_num"]').text
# print(shopnumele)
# if int(shopnumele) == 0:
#    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div/i').click()

driver.implicitly_wait(20)
# time.sleep(5)
# 购物车结算
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]').click()

# 确认提交订单
driver.implicitly_wait(20)
sub = driver.find_element_by_xpath('/html/body/div[14]/div/button').click()

driver.implicitly_wait(5)
# 选择支付方式
pay = driver.find_element_by_xpath('//*[@id="cart4_form"]/div/div/dl/dd/div/div[2]/ul/li[2]/div')
pay.click()
# 确认支付
ispay = driver.find_element_by_xpath('//*[@id="cart4_form"]/div/div/div/a')
ispay.click()

# 查看订单详情
# tishi = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/h3').text
# if tishi == ' 订单提交成功，我们将在第一时间给你发货！':
# driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a').click()

# 查看我的订单
driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[1]/a').click()

driver.implicitly_wait(10)
# 获取浏览器窗口
handles = driver.window_handles
driver.close()
# 切换到对应的窗口
driver.switch_to.window(handles[1])

# 获取订单的信息
orderele = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[4]/table[1]/tbody/tr[2]/td[1]/div/div[2]').text
print(orderele)

# 取消订单
driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[4]/table[1]/tbody/tr[1]/td/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div[6]/div[3]/a[1]').click()
driver.find_element_by_xpath('/html/body/div[7]/div[3]/a').click()

# 退出登录
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[2]').click()
