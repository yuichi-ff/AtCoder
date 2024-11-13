N,A,B = map(int,input().split())

def digitsum(n):
    sm = 0
    while(n!=0):
        sm += n % 10
        n = n // 10
    return sm


ans = 0
for n in range(1,N+1):
    if A <= digitsum(n) and digitsum(n) <= B:
        print(n)
        ans += n

print(ans)