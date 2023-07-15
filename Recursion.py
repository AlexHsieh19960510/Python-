# 1.遞迴
def a(n):                    # 建立函式 a，帶有參數 n
    if n == 0 or n == 1:     # 如果 n 等於 0 或 1
        return 1             # 回傳結果 1
    else:
        return n + a(n-1)    # 使用遞迴

print(a(3))                  # 執行結果為 6 ( 3+2+1 )


# 2.使用遞迴 vs 使用迭代操作
# 	                           遞迴	           迭代操作 ( 迴圈 )
# 程式碼長度	                精簡	           冗長
# 可能需要的區域變數	          少	            多
# 是否需要額外的 Stack 支持	    需要	           不需要
# 佔用的儲存空間	              少	            多
# 程式執行時間	            長 ( 較無效率 )	    短 ( 不用額外處理 push/pop )


# 3.n 階層
def a(n):                    # 建立函式 a，帶有參數 n
    if n == 0 or n == 1:     # 如果 n 等於 0 或 1
        return 1             # 回傳結果 1
    else:
        return n * a(n-1)    # 使用遞迴
print(a(4))                  # 執行結果為 24 ( 4x3x2x1 )


# 4.費波那契數列
def fib(n):                         # 建立函式 fib，帶有參數 n
    if n > 1:                       # 如果 n 大於 1
        return fib(n-1) + fib(n-2)  # 使用遞迴
    return n
for i in range(20):                 # 產生 20 個數字
    print(fib(i), end = ",")        # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181


# 5.最大公因數
def f(a, b):               # 建立函式 f，帶有參數 a 和 b
    if a % b == 0:         # 如果相除餘數為 0，回傳結果
        return b
    else:                  # 如果相除不為 0，表示還沒找到最大公因數
        return f(b, a % b) # 使用遞迴，參數 a 使用 b，b 使用 a 除以 b 的餘數
print(f(456, 48))          # 得到結果 24






























