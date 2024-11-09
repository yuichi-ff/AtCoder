N = int(input())

#１以上N以下の整数で約数が8個の物の個数を求めよ
ans = []
for i in range(1,N+1,2):
    amount = 0
    for j in range(1,i+1):
        if i % j == 0:
            amount += 1
    if amount == 8:
        ans.append(i)

print(len(ans))