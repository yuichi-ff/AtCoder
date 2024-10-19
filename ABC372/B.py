M = int(input())

ans = []
i = 10
while M > 0:
    while 3**i > M:
        M = M - 3**i
        ans.append(i)

print(len(ans))
print(*ans)