N,L,R = map(int,input().split())

arg = [i+1 for i in range(N)]
ans = []
ans.extend(arg[:L-1])

rev = arg[L-1:R]
rev.reverse()
ans.extend(rev)
ans.extend(arg[R:])

print(*ans)
