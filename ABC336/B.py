X = int(input())

print(len(str(bin(X)).split("1")[-1]))
# 解説のやつ：
# print(bin(X)[::-1].find("1"))