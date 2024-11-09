N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# iとjを合成
# i>=j のときAi,j i<j ー＞ Aj,i

# 元素1,1 1,2, 1,3 ... 1,N順 に合成した時のやつは？

i = 1

for j in range(1,N+1):
    if i >= j:
        i = A[i-1][j-1]
    else:
        i = A[j-1][i-1]
    
print(i)

# 言われたとおり実装するだけなのに……