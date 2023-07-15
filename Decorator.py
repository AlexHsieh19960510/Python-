# 1.裝飾器(1)
def a(func):
    print("makeup...")
    return func

def b():
    print("go!!!!")

b = a(b)
b()

# makeup...
# go!!!!


# 2.裝飾器(2)
def a(func):
    print("makeup...")
    return func

# 裝飾器寫在 b 的前面，表示裝飾 b
@a
def b():
    print("go!!!!")

b()
# makeup...
# go!!!!


# 3.多個裝飾器
def a1(func):
    print("1")
    return func

def a2(func):
    print("2")
    return func

def a3(func):
    print("3")
    return func

@a1
@a2
@a3
def b():
    print("go!!!!")

b()
# 3
# 2
# 1
# go!!!!


# 4.單一參數處理
def a(func):
    def c(m):             # 新增一個內部函式，待有一個參數
        print("makeup...")
        return func(m)      # 回傳 func(m)
    return c

@a
def b(msg):
    print(msg)

b("go!!!!")
# makeup...
# go!!!!


# 5.多個參數處理
def a(func):
    def c(*args, **kwargs):
        print(args)
        print(kwargs)
        print("ok...")
        return func(*args, **kwargs)
    return c

@a
def b(*args, **kwargs):
    print("go!!!!")

b([123, 456], x = 1, y = 2, z = 3)

# ([123, 456],)
# {'x': 1, 'y': 2, 'z': 3}
# ok...
# go!!!!



























