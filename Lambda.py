# 1.匿名函式的特性
# 匿名函式不需要定義名稱，一般函式需定義名稱。
# 匿名函式只能有一行運算式，一般函式可以有多行運算式。
# 匿名函式執行完成後自動回傳結果，一般函式加上 return 關鍵字才能回傳結果。


# 2.使用匿名函式 lambda
def hello(title):
    print(title)

hello("oxxo")      # oxxo
(lambda title: print(title))("oxxo")   # oxxo


# 3.使用多個參數(1)
def hello(x, y):
    return x + y

a = hello(1,2)
b = (lambda x, y: x + y)(1,2)
print(a)    # 3
print(b)    # 3


# 4.使用多個參數(2)
def a(x, y):
    return x + y
b = lambda x, y: x + y
print(a(1,2))   # 3
print(b(1,2))   # 3


# 5.搭配 for 迴圈
def x(n):
    a = list(range(n))
    return a
y = lambda n: [i for i in range(n)]   # 計算後回傳串列結果
print(x(5))    # [0, 1, 2, 3, 4]
print(y(5))    # [0, 1, 2, 3, 4]


# 6.搭配 if 判斷式
def y(n):
    if n < 10:
        return True
    else:
        return False
x = lambda n: True if n < 10 else False   # 判斷是否小於 10，回傳 True 或 False
print(x(5))   # True
print(y(5))   # True


# 7.搭配 map 方法
a = [1,2,3,4,5,6,7,8,9]
b = map(lambda x: x * x, a)
print(list(b))    # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 8.搭配 filter 方法
a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x: x > 5, a)
print(list(b))    # [6, 7, 8, 9]


# 9.搭配 sorted 方法
a = [[1,2],[4,3],[5,1],[9,2],[3,7]]
b = sorted(a, key = lambda x: x[1])
print(list(b))    # [[5, 1], [1, 2], [9, 2], [4, 3], [3, 7]]
































