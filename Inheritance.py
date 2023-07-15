# 1.Inheritance
class father():         # fatehr 類別
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):          # son 類別繼承了 fatehr 類別裡所有的方法
    def language(self):     # son 類別具有 language 的方法
        print("chinese")    # 從 father 繼承了五官，然後自己學會講中文

oxxo = son()                # 設定 oxxo 為 son()
print(oxxo.eye)             # 印出 2
oxxo.language()             # 印出 chinese


# 2.繼承時會覆寫方法
class father():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):
    def __init__(self):   # 使用了 __init 的方法
        self.eye = 100

oxxo = son()
print(oxxo.eye)    # 100
print(oxxo.ear)    # 發生錯誤  'son' object has no attribute 'ear'


# 3.super()
class father():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):
    def __init__(self):
        super().__init__()   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.eye = 100       # 如果屬性相同，則覆寫屬性

oxxo = son()
print(oxxo.eye)              # 100
print(oxxo.ear)              # 2


# 4.多重繼承(1)
class father():          # father 類別
    def __init__(self):  # father 的方法
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class mother():          # mother 類別
    def language(self):  # mother 的方法
        print("english")
    def skill(self):
        print("painting")

class son(father, mother):    # 繼承 father 和 mother
    def play(self):           # son 自己的方法
        print("ball")

oxxo = son()
print(oxxo.eye)        # 2
oxxo.skill()           # painting
oxxo.play()            # ball


# 5.多重繼承(2)
class a():
    def says(self):
        print("a")

class b():
    def says(self):
        print("b")

class c(a, b):    # 先讀取 a 再 b，就會將 a 裡的方法，覆寫 b 裡同名的方法
    pass

class d(b, a):    # 先讀取 b 再 a，就會將 b 裡的方法，覆寫 a 裡同名的方法
    pass

ccc = c()
ddd = d()
ccc.says()    # a
ddd.says()    # b


# 6.多層繼承
class grandpa():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class father(grandpa):
    def language(self):
        print("english")
    def skill(self):
        print("painting")

class son(father):
    def play(self):
        print("ball")

oxxo = son()
print(oxxo.eye)    # 2
oxxo.skill()       # painting
oxxo.play()        # ball


# 7.私有方法 ( 雙底線 )
class grandpa():
    def __init__(self):
        self.mouth = 1
    def __money(self):     # 建立一個私有方法 __money
        print("$1000")
    def getMoney(self):    # 建立一個 getMoney 的方法，執行私有方法 __money
        self.__money()

class father(grandpa):
    def skill(self):
        print("painting")

class son(father):
    def play(self):
        print("ball")

oxxo = son()
oxxo.getMoney()         # $1000
oxxo.__money()          # 發生錯誤  'son' object has no attribute '_money'
























