# 1.定義函式(1)
def hello():
    print("hello")
hello()    # 執行函式，印出 hello


# 2.定義函式(2)
hello()
def hello():
    print("hello")   # 發生錯誤 name 'hello' is not defined


# 3.函式參數(1)
def hello(msg):
    print(msg)

hello("hello")        # hello
hello("good morning") # good morning


# 4.函式參數(2)
def hello(x,y):
    z = x + y
    print(z)

hello(1,2)    # 3
hello(5,6)    # 11


# 5.參數預設值
def hello(x,y = 10):
    z = x + y
    print(z)

hello(1,2)    # 3
hello(5)      # 15


# 6.關鍵字引數(1)
def hello(name, age):
    msg = f"{name} is {age} years old"
    print(msg)

hello("oxxo",18)     # oxxo is 18 years old
hello(18,"oxxo")     # 18 is oxxo years old ( 因為 18 和 oxxo 對調，所以結果就會對調 )
hello(age = 18,name = "oxxo")   # oxxo is 18 years old ( 使用關鍵字引數，結果就會是正確的 )


# 7.關鍵字引數(2)
def test(a, start = 0, end = 3):
    for i in a[start:end]:
        print(i)

b = [1,2,3,4,5]
test(b, start = 2, end = len(b))  # 3 4 5
test(b)             # 1 2 3


# 8.函式回傳值(1)
def a(x, y):
    result = x + y * 2
    return result

b = a(1,2)
c = a(2,3)
print(b)   # 5
print(c)   # 8


# 9.函式回傳值(2)
def a(x):
    result = 0
    while result < 10:
        result = result + x
        if result == 5:
            return result
    return result

b = a(1)
c = a(2)
print(b)   # 5
print(c)   # 10


# 10.函式回傳值(3)
def test(x, y, z):
    return x + 1, y + 1, z + 1

a, b, c = test(1, 2, 3)    # 賦值給「同樣數量」的變數
print(a)    # 2
print(b)    # 3
print(c)    # 4


# 11.函式回傳值(4)
def test(x, y, z):
    return x + 1, y + 1, z + 1

a = test(1, 2, 3)
print(a)    # (2, 3, 4)


# 12.函式內的函式
def hello(n, msg):
    def h1():       # 內部函式
        return msg
    def h2():       # 內部函式
        return msg * 2
    if n == 1:
        print(h1())
    if n == 2:
        print(h2())
hello(1, "ok")   # ok
hello(2, "ok")   # okok
print(h2())      # 發生錯誤 name 'h2' is not defined


# 13.函式內的變數(1)
a = 123           # 全域變數 a
b = 123           # 全域變數 b
def hello(msg):
    a = msg         # 區域變數 a，更動區域變數不影響全域變數
    print(a)
    global b        # 宣告變數 b 是使用全域變數 b，更動變等同更動全域變數
    b = msg
hello(456)        # 456
print(a)          # 123
print(b)          # 456 被更改為 456


# 14.函式內的變數(2)
def hello(msg):
    a = 123
    b = 123
    def h1():
        nonlocal a    # 宣告 a 為自由變數
        a = a + msg
        print(a)
    def h2():
        b = b + msg
        print(b)
    h1()            # 579
    h2()            # 發生錯誤  local variable 'b' referenced before assignment
hello(456)


# 15.*args、**kwargs 運算子(1)
def test(*args):
    print(args)

test(1,2,3,"a","b","c")

# (1,2,3,"a","b","c")


# 16.*args、**kwargs 運算子(2)
def test(**kwargs):
    print(kwargs)

test(name = "oxxo",age = 18,like = "book")

 # {"name": "oxxo", "age": 18, "like": "book"}


# 17.*args、**kwargs 運算子(3)
def a(*args, **kwargs):
    print(args)
    print(kwargs)

a([123, 456], x = 1, y = 2, z = 3)

# ([123, 456],)
# {'x': 1, 'y': 2, 'z': 3}


# 18.*args、**kwargs 運算子(4)
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = {"x":1,"y":2,"z":3}
d = {"x","y","z"}

print(*a)   # 1 2 3 4 5
print(*b)   # 1 2 3 4 5
print(*c)   # x y z
print(*d)   # x y z


# 19.使用 pass(1)
def test():
    pass


# 20.使用 pass(2)
a = int(input(">"))
if a>10:
    pass       # 如果輸入的數字大於 10，不做任何事情
else:
    print(a)


