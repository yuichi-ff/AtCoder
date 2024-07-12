N = int(input())
T = [list(map(int,input().split())) for _ in range(N)]
T.insert(0,[0,0,0])

ans = "Yes"
for i in range(1,len(T)):
    dt = T[i][0]-T[i-1][0]
    dist = abs(T[i][1]-T[i-1][1])+abs(T[i][2]-T[i-1][2])
    if dist > dt or dt%2 != dist%2:
        ans = "No"
        break

print(ans)