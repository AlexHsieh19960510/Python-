# 1.import
import datetime
print(datetime.datetime.now())   # 2023-07-15 17:32:23.422895
print(datetime.date.today())     # 2023-07-15


# 2.from 模組名稱 import 方法
from datetime import date
print(date.today())     # 2023-07-15


# 3.as 替模組新增別名
import datetime as dd
print(dd.datetime.now())   # 2023-07-15 17:32:23.422895
print(dd.date.today())     # 2023-07-15


# 4.建立自己的模組(1)
# 透過 main.py 匯入 ok.py，執行 ok.py 裡的 talk 函式
# ok.py

def talk(msg):
  print(msg)
  
# main.py

import ok
ok.talk("hi")   # hi


# 5.建立自己的模組(2)
# 可以透過「from 模組名稱 import 方法」單獨匯入
# ok.py

def talk(msg):
    print(msg)

def count(x, y):
    print(int(x) + int(y))

name = "oxxo"
age = 18

# main.py

from ok import count
from ok import name
count(1,2)      # 3
print(name)     # oxxo


# 6.模組的路徑
# 將 ok.py 放在與 main.py 同層的 module 的 test 資料夾裡
from module.test import ok
ok.count(1,2)      # 3
print(ok.name)     # oxxo






















