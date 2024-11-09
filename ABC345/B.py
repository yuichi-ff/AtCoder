X = int(input())

def div_ceil(a,b): # 公式暗記 aをbで割った結果を整数に切り上げる
    return (a+b-1)//b

print(div_ceil(X,10))