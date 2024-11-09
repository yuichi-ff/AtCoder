A,B,K = map(int,input().split())

"""
ans = []
for i in range(1,100+1):
    if A%i == 0 and B%i == 0:
        ans.append(i)

print(ans[len(ans)-K])

"""
#改良版（デカい方から入れていけばans[K-1]でK番目に大きい数字をば可能）
ans = []
for i in range(100,0,-1): 
    if A%i == 0 and B%i == 0:
        ans.append(i)

print(ans[K-1])
