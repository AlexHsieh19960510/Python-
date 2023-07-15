# 1.產生器
# 產生器是記錄「產生值的方法」，而不是記錄值。
# 使用產生器中「產生的值只能取用一次」，無法重新啟動或重新取得 ( 因為不會紀錄 )。


# 2.產生器表示式(1)
a = [i for i in range(10)]  # 串列生成式
b = (i for i in range(10))  # 產生器表示式
print(a)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)   # <generator object <genexpr> at 0x7fbb6facba50>


# 3.產生器表示式(2)
a = [i ** 2 for i in range(10)]
for i in a:
    print(i, end=" ")    # 0 1 4 9 16 25 36 49 64 81
for i in a:
    print(i, end=" ")    # 0 1 4 9 16 25 36 49 64 81
print()
b = (i ** 2 for i in range(10))
for i in b:
    print(i, end=" ")    # 0 1 4 9 16 25 36 49 64 81
for i in b:
    print(i, end=" ")    # 取不到值


# 4.產生器表示式(3)
a = (i ** 2 for i in range(10))  # 串列生成式
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 4
print(next(a))  # 9
print(next(a))  # 16
print(next(a))  # 25
print(next(a))  # 36
print(next(a))  # 49
print(next(a))  # 64
print(next(a))  # 81
print(next(a))  # 發生錯誤，因為取不到值


# 5.yield 陳述式(1)
def f(max):
    n = 0
    a = 2
    while n < max:
        print(a)
        a = a ** 2
        n = n + 1
f(5)                # 2 4 16 256 65536


# 6.yield 陳述式(2)
def f(max):
    n = 0
    a = 2
    while n < max:
        yield(a)     # 換成 yield
        a = a ** 2
        n = n + 1
f(5)                # <generator object f at 0x7fbb6facba50>


# 7.yield 陳述式(3)
def f():
    print(1)
    print(2)
    print(3)
f()    # 一次印出 1、2、3


# 8.yield 陳述式(4)
def f():
    yield(1)       # 使用 yield
    yield(2)
    yield(3)
g = f()          # 賦值給變數 g
print(next(g))   # 1
print(next(g))   # 2
print(next(g))   # 3


# 9.yield 陳述式(5)
def f():
    yield(1)
    yield(2)
    yield(3)
print(next(f()))   # 1
print(next(f()))   # 1
print(next(f()))   # 1


# 10.yield 陳述式(6)
def f(max):
    n = 0
    while n < max:
        yield(n)
        n = n + 1
g = f(10)
a = []
b = []
for i in range(5):
    a.append(next(g))
for i in range(5):
    b.append(next(g))
print(a)     # [0, 1, 2, 3, 4]
print(b)     # [5, 6, 7, 8, 9]


# 11.使用產生器找質數(1)
a = range(2,100)                            # 產生 2～100 的串列
print(*a)
b = [i for i in a if i == a[0] or i % a[0] > 0]   # 找出第一個質數，並將串列裡該質數的倍數剔除
print(*b)
c = [i for i in b if i == b[1] or i % b[1] > 0]   # 找出第二個質數，並將串列裡該質數的倍數剔除
print(*c)
d = [i for i in c if i == c[2] or i % c[2] > 0]   # 找出第三個質數，並將串列裡該質數的倍數剔除
print(*d)


# 12.使用產生器找質數(2)
def gg(max):                   # 定義一個 gg 函式
    s = set()                    # 設定一個空集合
    for n in range(2,max):       # 從 range(2, max) 當中開始依序找質數
        if all(n % i > 0 for i in s):  # 判斷如果 i 已經存在於集合，且除以集合中的值會有餘數 ( 整除表示非質數 )
            s.add(n)                 # 將該數字加入集合 ( 表示質數 )
            yield n                  # 使用 yield 記錄狀態
print(*gg(100))                # 印出結果




















