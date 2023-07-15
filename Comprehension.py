# 1.串列生成式(1)
# result = [expression for item in iterable]
# result：生成的新串列。
# expression：生成的項目。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。


# 2.串列生成式(2)
# 單純寫法
a = []
for i in range(1, 10):
    a.append(i * i)
print(a)      # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用串列生成式
b = [j * j for j in range(1,10)]
print(b)      # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 3.串列生成式(3)
# 單純寫法
a = [10,20,30,40,50,60,70,80,90]
b = []
for i in a:
    b.append(max(a) - i)     # 用 a 的最大值減去每個項目
print(b)                   # [80, 70, 60, 50, 40, 30, 20, 10, 0]

# 使用串列生成式
a = [10,20,30,40,50,60,70,80,90]
b = [max(a) - i for i in a]
print(b)                   # [80, 70, 60, 50, 40, 30, 20, 10, 0]


# 4.串列生成式(4)
# 單純寫法
# 將兩層 for 迴圈的 i 和 j 加在一起，變成新串列的項目
a = []
for i in "abc":
    for j in range(1,4):
        a.append(i + str(j))
print(a)        # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# 使用串列生成式
a = [i + str(j) for i in "abc" for j in range(1, 4)]
print(a)        # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


# 5.串列生成式搭配 if(1)
# 單純寫法
a = []
for i in range(1,10):
    if i % 2 == 0:
        a.append(i)   # 取出偶數放入變數 a
print(a)              # [2, 4, 6, 8]

# 使用串列生成式
a = [i for i in range(1, 10) if i % 2 == 0]
print(a)           # [2, 4, 6, 8]


# 6.串列生成式搭配 if(2)
# 單純寫法
a = []
for i in range(1,10):
    if i % 2 == 0:
        a.append(i)   # 取出偶數放入變數 a
    else:
        a.append(100) # 如果是奇數，將 100 放入變數 a
print(a)          # [100, 2, 100, 4, 100, 6, 100, 8, 100]

# 使用串列生成式
a = [i if i % 2 == 0 else 100 for i in range(1, 10)]
print(a)          # [100, 2, 100, 4, 100, 6, 100, 8, 100]


# 7.字典生成式(1)
# result = {key: value for item in iterable}
# result：生成的新字典。
# key：生成的鍵。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。


# 8.字典生成式(2)
# 單純寫法
a = {}
for i in range(1,10):
    a[i] = i * i   # 將 i*i 對應指定的鍵
print(a)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 使用字典生成式
a = {i:i * i for i in range(1,10)}
print(a)       # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# 9.集合生成式(1)
# result = {value for item in iterable}
# result：生成的新集合。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。


# 10.集合生成式(2)
# 單純寫法
a = set()
for i in range(1,10):
    a.add(i * i)   # 將 i*i 新增到集合裡
print(a)         # {64, 1, 4, 36, 9, 16, 49, 81, 25}

# 使用串列生成式
a = {i * i for i in range(1,10)}
print(a)       # {64, 1, 4, 36, 9, 16, 49, 81, 25}


# 11.元組 ( 數組 ) 生成式(1)
# variable = tuple(value for item in iterable)
# variable：型別為 tuple 的變數。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。


# 12.元組 ( 數組 ) 生成式(2)
a = tuple(i for i in range(10))
print(a)   # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# 元組 ( 數組 ) 生成式(3)
a = tuple(i * i for i in range(10) if i > 5)
print(a)   # (36, 49, 64, 81)















