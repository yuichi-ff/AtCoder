A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# 内積が０
# ベクトル → 終点-始点
# I = x1*x2 + y1*y2

def is90(center,AA,BB):
    Av = (AA[0]-center[0], AA[1]-center[1])
    Bv = (BB[0]-center[0], BB[1]-center[1])
    
    return Av[0]*Bv[0] + Av[1]*Bv[1] == 0

ans = "No"
if is90(A,B,C) or is90(B,A,C) or is90(C,A,B):
    ans = "Yes"

print(ans)
