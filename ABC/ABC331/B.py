N,S,M,L = map(int,input().split())

ans = 10**8
for s in range(101):
    for m in range(101):
        for l in range(101):
            if s*6+m*8+l*12 >= N:
                ans = min(ans,s*S+m*M+l*L)
            
print(ans)