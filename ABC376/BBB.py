N,Q = map(int,input().split())

hands = [1,2]
ans=0

for _ in range(Q):
    H, T = input().split()
    H = 0 if H=="L" else 1
    T = int(T)

    to = (T-hands[H]) % N
    ng = (T-hands[(H+1)%2]) % N
    
    if ng < to:
        ans += N-to
    else:
        ans += to

    hands[H] = T

print(ans)