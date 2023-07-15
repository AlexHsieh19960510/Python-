# 1.class
class human():
  def __init__(self):  # 建立預設屬性的寫法
    self.eye = 2       # 兩個眼睛
    self.ear = 2       # 兩個耳朵
    self.nose = 1      # 一個鼻子
    self.mouth = 1     # 一張嘴巴

oxxo = human()         # 製作一個名為 oxxo 的物件
print(oxxo.eye)        # 得到 2 ( 印出 oxxo 的 eye 屬性 )。


# 2.class-pass
class human():
    pass        # 使用 pass 可以建立一個空類別


# 3.預設屬性
class human():
    def __init__(self):  # 建立預設屬性的寫法
        self.eye = 2       # 兩個眼睛
        self.ear = 2       # 兩個耳朵
        self.nose = 1      # 一個鼻子
        self.mouth = 1     # 一張嘴巴


# 4.自訂屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):      # 定義 say
        print(msg)
    def play(self, thing):   # 定義 play
        print(thing)

oxxo = human()
oxxo.say("hello")          # hello
oxxo.play("baseball")      # baseball


# 5.外部定義
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(msg)
    def play(self, thing):
        print(thing)

human.hand = 2    # 定義 hand 屬性
human.leg = 2     # 定義 leg 屬性

oxxo = human()
print(oxxo.hand)  # 2
print(oxxo.leg)   # 2


# 6.self 讀取到這個物件的所有屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(f"{self.name} say: {msg}")   # 使用 self.name 取得 name 屬性的值
    def play(self, thing):
        print(thing)

oxxo = human()
oxxo.name = "oxxo"   # 設定 name 屬性
oxxo.say("hello")    # oxxo say: hello


# 7.多個物件同一個類別(1)
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(f"{self.name} say: {msg}")
    def play(self, thing):
        print(thing)

oxxo = human()        # 定義 oxxo
gkpen = human()       # 定義 gkpen
oxxo.name = "oxxo"    # oxxo 的名字叫做 oxxo
oxxo.age = 18         # oxxo 的 age 為 18

gkpen.name = "gkpen"  # gkpen 的名字叫做 gkpen
gkpen.weight = 70     # gkpen 的 weight 為 70

oxxo.say("hello")    # oxxo say: hello
print(oxxo.age)      # 18
gkpen.say("song")    # gkpen say: song
print(gkpen.weight)  # 70


# 8.多個物件同一個類別(2)
class human():
    def __init__(self, age, weight):    # 新增 age 和 weight 參數
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
        self.age = age             # 讀取參數，變成屬性
        self.weight = weight       # 讀取參數，變成屬性
    def say(self, msg):
        print(f"{self.name} say: {msg}")
    def play(self, thing):
        print(thing)

oxxo = human(18, 68)            # 建立物件時，設定參數數值
gkpen = human(15, 70)           # 建立物件時，設定參數數值
print(oxxo.age, oxxo.weight)    # 18, 68
print(gkpen.age, gkpen.weight)  # 15, 70


# 9.覆寫屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(f"{self.name} say: {msg}")
    def play(self, thing):
        print(thing)

oxxo = human()
oxxo.play = "???"  # 覆寫 play 屬性
print(oxxo.play)   # ???


# 10.@property 唯讀屬性
class a:
    def a(self):
        return "aaaaa"
    @property
    def b(self):
        return "bbbbb"

oxxo = a()
oxxo.a = "12345"
print(oxxo.a)   # 12345
oxxo.b = "12345"
print(oxxo.b)   # 發生錯誤  can't set attribute













