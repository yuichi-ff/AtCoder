N,M = map(int,input().split())
koma = [list(map(int,input().split())) for _ in range(M)]
"""
マス 
(i+2,j+1) に置かれている
マス 
(i+1,j+2) に置かれている
マス 
(i−1,j+2) に置かれている
マス 
(i−2,j+1) に置かれている
マス 
(i−2,j−1) に置かれている
マス 
(i−1,j−2) に置かれている
マス 
(i+1,j−2) に置かれている
マス 
(i+2,j−1) に置かれている
"""

def addbut(i,j,setto : set):
    i -= 1
    j -= 1
    if (i<0 or j<0) or (i>=N or j>=N):
        return
    setto.add((i,j))

anslist = set()

for aaaa in range(M):
    i,j = (koma[aaaa][0],koma[aaaa][1])
    i -= 1
    j -= 1

    t,m=i,j
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i+2,j+1
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i+1,j+2
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i-1,j+2
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i-2,j+1
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i-2,j-1
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i-1,j-2
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i+1,j-2
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

    t,m=i+2,j-1
    if not((t<0 or m<0) or (t>=N or m>=N)):
        anslist.add((t,m))

#print(anslist)
ans = (N*N) - len(anslist)

print(ans)