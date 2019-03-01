from homework.class6 import Sort


list1 = [1, 5, 2, 11, 2, 5, 8, 3]
Sort.quicksort(list1, 0, len(list1)-1)
print("快速排序：", end='')
print(list1)

list2 = [22, 5, 4, 11, 6, 14, 9, 3]
Sort.selectSort(list2)
print("选择排序：", end='')
print(list2)

list3 = [123, 122, 145, 11, 33, 64, 38, 79]
Sort.bubbleSort(list3)
print("冒泡排序：", end='')
print(list3)

print("杨辉三角：")
Sort.printYh(5)

# # 快速排序
# def quicksort(List, left, right):
#     left1 = left
#     right1 = right
#     # 基准值
#     base = List[right]
# if
# while left < right:
#     # 从左往右循环找
#     while left < right:
#         # 找到后进行交换位置, 找到后右下标左移一位
#         if List[left] > base:
#             List[left], List[right] = List[right], List[left]
#             right = right - 1
#             # 找到之后进行从右往左的比较操作
#             break
#         else:
#             left = left + 1
#     # 从右往左找 ，找到后左下标右移一位
#     while left < right:
#         if List[right] < base:
#             List[left], List[right] = List[right], List[left]
#             left = left + 1
#             break
#         else:
#             right = right - 1

