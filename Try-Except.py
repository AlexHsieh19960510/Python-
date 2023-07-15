# 1.try-except
try:                      # 使用 try，測試內容是否正確
    a = input("輸入數字：")
    print(a + 1)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    print("發生錯誤")
print("hello")


# 2.try-except-pass
try:                      # 使用 try，測試內容是否正確
    a = input("輸入數字：")
    print(a + 1)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    pass                  # 略過
print("hello")


# 3.
# 錯誤資訊	                說明
# NameError	         使用沒有被定義的對象
# IndexError	     索引值超過了序列的大小
# TypeError	         數據類型 ( type ) 錯誤
# SyntaxError	     Python 語法規則錯誤
# ValueError	     傳入值錯誤
# KeyboardInterrupt	 當程式被手動強制中止
# AssertionError	 程式 asset 後面的條件不成立
# KeyError	         鍵發生錯誤
# ZeroDivisionError	 除以 0
# AttributeError	 使用不存在的屬性
# IndentationError	 Python 語法錯誤 ( 沒有對齊 )
# IOError	         Input/output異常
# UnboundLocalError	 區域變數和全域變數發生重複或錯誤


# 4.一個try多個except(1)
try:
    print(a)
except TypeError:              # 可以有多個 except，但程式執行時會依據 Error type 執行特定 except
    print("型別發生錯誤")
except NameError:              # 可以有多個 except，但程式執行時會依據 Error type 執行特定 except
    print("使用沒有被定義的對象")
print("hello")


# 5.一個try多個except(2)
try:
    print(1 / 0)
except TypeError:                      # 可以有多個 except，但程式執行時會依據 Error type 執行特定 except
    print("型別發生錯誤")
except NameError:                      # 可以有多個 except，但程式執行時會依據 Error type 執行特定 except
    print("使用沒有被定義的對象")
except Exception:                      # 不知道 Error type，只想印出錯誤資訊，可以使用 except Exception
    print("不知道怎麼了，反正發生錯誤惹")
print("hello")


# 6.except Exception as e
try:
    a = 1
    b = "1"
    print(a + b)
except Exception as e:  # except Exception as e 也能將所有的錯誤資訊全部印出
    print(e)


# 7.rasie強制中斷(1)
try:
    a = int(input("輸入 0～9："))
    if a > 9:       # 如果輸入的 a 大於 9
        raise       # 強制中斷，拋出錯誤資訊席
    print(a)
except :
    print("有錯誤喔～")   # 收到錯誤訊息，顯示錯誤


# 8.rasie強制中斷(2)
try:
    a = int(input("輸入 0～9："))
    if a > 10:
        raise ValueError("數字不在範圍內")  # raise 'error type'("msg")
    print(a)
except ValueError as msg:    # 如果輸入範圍外的數字，執行這邊的程式
    print(msg)
except :                     # 如果輸入的不是數字，執行這邊的程式
    print("有錯誤喔～")   
print("繼續執行")


# 9.assert強制中斷
try:
    a = int(input("輸入 0～9："))
    if a > 10:
        assert False, "數字不在範圍內"  # assert False, "msg"
    print(a)
except AssertionError as msg:
    print(msg)
except :
    print("有錯誤喔～")   
print("繼續執行")


# 10.else、finally
try:
    a = int(input("輸入 0～9："))
    if a > 10:
        raise
    print(a)
except :
    print("有錯誤喔～")   
else:
    print("沒有錯！繼續執行！")       # 完全沒錯才會執行這行
finally:
    print("管他有沒有錯，繼續啦！")    # 不論有沒有錯都會執行這行 









