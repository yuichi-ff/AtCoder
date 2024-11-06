A,B = map(int,input().split())

if A==B:
    print(1)
    exit()

ans = 0
if (max(A,B)-min(A,B)) % 2 == 0:
    ans += 1

print(ans+2)
