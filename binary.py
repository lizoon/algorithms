# n, *a = list(map(int, input().split()))
# k, *b = list(map(int, input().split()))
#
#
# def func(a, x):
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if x == a[mid]:
#             return mid + 1
#         elif x > a[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
#
# print(*[func(a, x) for x in b])
#


#
# from math import sqrt
# c = float(input())
#
#
# def f(x):
#     return x*x + sqrt(x)
#
#
# def funcy(c):
#     low = 0
#     high = c
#     while low <= high:
#         x = (low + high) / 2
#         y = float('{:.8f}'.format(f(x)))
#         if y == c:
#             return x
#         if y < c:
#             low = x
#         else:
#             high = x
#     return -1
#
#
# y = funcy(c)
# print('{0:.9f}'.format(y))


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


fact(5)