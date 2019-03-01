# -*-encoding=UTF-8 -*-


# 快速排序
def quicksort(List, left, right):
    # 记录初始左右边界
    left1 = left
    right1 = right
    # 基准值
    base = List[right]

    # 反复执行，直到
    while left < right:
        # 从左往右循环找
        while left < right:
            # 找到后进行交换位置, 找到后右下标左移一位
            if List[left] > base:
                List[left], List[right] = List[right], List[left]
                right = right - 1
                # 找到之后进行从右往左的比较操作
                break
            else:
                left = left + 1
        # 从右往左找 ，找到后左下标右移一位
        while left < right:
            if List[right] < base:
                List[left], List[right] = List[right], List[left]
                left = left + 1
                break
            else:
                right = right - 1

    # 使用递归分别排序两侧的数据
    if left1 < left:
        quicksort(List, left1, left - 1)

    if right < right1:
        quicksort(List, right + 1, right1)
    # 函数已经修改了list的地址
    # return list


# 选择排序
def selectSort(list):
    for i in range(0, len(list)):
        # 标记最小值下标
        mixindex = i
        for j in range(i + 1, len(list)):
            if list[mixindex] > list[j]:
                # 标记最小值
                mixindex = j

        list[mixindex], list[i] = list[i], list[mixindex]



# 冒泡排序
def bubbleSort(list):
    for i in range(0, len(list)):
        # 因为i是从0开始，j应该从1开始，可以与j-1进行比较，每次比较的最大值都会在本次列表的最后
        for j in range(1, len(list) - i):
            if list[j - 1] > list[j]:
                # 交换位置
                list[j - 1], list[j] = list[j], list[j - 1]



# 输出杨辉三角
def printYh(num):
    # 定义上一行
    ls = [1]
    # 定义下一行
    lx = [1, 1]
    i = 0
    while i < num + 1:
        a = i
        while a < num:
            print('%3s' % "", end="")
            a += 1
        b = 0
        while b < len(ls):
            # m = 2 * r
            # print(m)
            print('%6s' % ls[b], end="")
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

    return lx
