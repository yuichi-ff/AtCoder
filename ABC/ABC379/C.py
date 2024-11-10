N,M = map(int,input().split())
Xs = list(map(int,input().split()))
As = list(map(int,input().split()))

if sum(As) > N:
    print(-1)
    exit()

ans = 0

# 重複してたらa+1
for i in range(M):
    x = Xs[i]
    a = As[i]
    for j in range(a):
        if x+j < M:
            #print("target:",Xs[x+j],"genjusho:",x+a)
            if Xs[x+j] < (x+a):
                As[x+j] += 1

#まずそうなら-1
for i in range(0,M-1):
    x = Xs[i]
    a = As[i]
    if x+(a-1) < Xs[i+1]-1:
        print(-1)
        exit()

#print(As)

# かかるターン数： 石の数n -> (n-1)((n-1)+1)/2
for i in range(M):
    x = Xs[i]
    a = As[i]
    a -= 1
    #print((a*(a+1))/2)
    ans += (a*(a+1))/2

print(int(ans))