N,M = map(int,input().split())
H = list(map(int,input().split()))

used = 0
ans = 0
for h in H:
    used += h
    if used > M:
        break
    ans += 1
print(ans)