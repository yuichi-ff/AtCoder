N = int(input())
MP = [list(map(int,input().split())) for _ in range(N)]

for mp in MP:
    for i in range(N):
        if mp[i] == 1:
            print(i+1, end=" ")
    print()