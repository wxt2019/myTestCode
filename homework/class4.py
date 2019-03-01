# coding = utf-8
import requests
import json
#获取网页
result = requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/"
                      "api.php", "query=114.241.219.238&co="
                       "&resource_id=6006&t=1546057250896&ie=utf8&oe=gbk&cb=op_aladdin_"
                        "callback&format=json&tn=baidu&cb=jQuery11020841719906598206_"
                        "1546057183006&_=1546057183012")
# 获取网页的内容
result = result.text
print(result)
print(type(result))
# 截取{}中的数据
result = result[result.find("{"):result.rfind("}")+1]
# 字符创转变成dict类型
result = json.loads(result)
print(result)
print(type(result))
location = result["data"][0]["location"]
print("IP所在位置：" + location)


height = [127, 234, 124, 156, 178, 121, 199, 231,121]
print("***************************选择降序排序for方法********************************")
# 倒序排列
l = len(height)
for i in range(0, l):
    # 记录最大的下标
    tem = i
    for j in range(i+1, l):
        if height[tem] < height[j]:
            # 交换最大值下标
            tem = j

    height[tem], height[i] = height[i], height[tem]

print(height)

print("***************************选择降序排序while方法******************************")
height2 = [127, 222, 124, 168, 178, 190, 199, 231, 158]
l2 = len(height2)
print(l2)
i = 0
while i < l2:
    tem = i
    j = i+1
    while j < l2:
        if height2[tem] < height2[j]:
            # 交换最大值下标
            tem = j
            # print(tem)
        j += 1

    height2[tem], height2[i] = height2[i], height2[tem]
    i += 1
print(height2)


print("***************************冒泡降序排序for方法********************************")

height3 = [127, 234, 124, 156, 178, 121, 199, 231, 121]
l3 = len(height3)
print(l3)
for i in range(0, l3-1):
    # 比较交换排序
    for j in range(1, l3-i):
        if height3[j-1] < height3[j]:
            height3[j-1], height3[j] = height3[j], height3[j-1]
print(height3)

print("***************************冒泡升序叙排序while方法****************************")
height4 = [127, 234, 124, 156, 178, 121, 199, 231, 121, 100]
l4 = len(height4)
i = 0
while i < l4:
    j = 1
    while j < l4 - i:
        if height4[j - 1] > height4[j]:
            height4[j - 1], height4[j] = height4[j], height4[j - 1]
        j += 1
    i += 1
print(height4)

print("*******************************杨辉三角for方法********************************")

# 定义上一行
ls = [1]
# 定义下一行
lx = [1, 1]
# 定义行数
num = 6
for i in range(0, num + 1):
    # 输出每行空格
    for a in range(i, num):
        print("%2s" % "", end="")

    # 格式化输出每行的数据
    for b in range(0, len(ls)):
        print("%4s" % ls[b], end="")
    # 换行
    print()
    for j in range(0, i + 2):
        # 一行两端值都是1
        if j == 0 or j == i + 1:
            lx[j] = 1
        else:
            # 等于上一行两值之和
            lx[j] = ls[j - 1] + ls[j]
    # 赋值给上一行
    ls = lx[0:]
    # 下一行值个数加1
    lx.append(1)

print("******************************杨辉三角while方法*******************************")

# 定义上一行
ls = [1]
lx = [1, 1]
# 定义杨辉三角的次数
yh = 10
i = 0
while i < yh + 1:
    a = i
    while a < yh:
        print("%3s" % "", end="")
        a += 1
    b = 0
    while b < len(ls):
        print("%-6s" % ls[b], end="")
        b += 1
    print()
    j = 0
    while j < i + 2:
        if j == 0 or j == i + 1:
            lx[j] = 1
        else:
            lx[j] = ls[j] + ls[j - 1]
        j += 1
    ls = lx[0:]
    lx.append(1)
    i += 1
