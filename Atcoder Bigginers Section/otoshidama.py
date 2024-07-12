N, Y = map(int,input().split())

a,b,c = (0,0,0)

"""
for a in range(N):
    for b in range(N):
        for c in range(N):
            total = 10000*a + 5000*b + 1000*c
            if a+b+c == N and total == Y:
                print(a,b,c)
                exit()"""


for a in range(N+1):
    for b in range(N+1):
        c = N - (a+b)
        total = (10000*a) + (5000*b) + (1000*c)
        if c >= 0 and  total == Y:
            print(a,b,c)
            exit()

print(-1,-1,-1)