N,Q = map(int,input().split())
HT = [list(input().split()) for _ in range(Q)]

for i in range(len(HT)):
    HT[i][0] = 0 if HT[i][0]=="L" else 1
    HT[i][1] = int(HT[i][1])

def kouho(current,to):
    A = abs(to - current)
    B = (to-1)+(Q-to)
    return (A,B)

hands = [1,2] #左手、右手

ring = [i for i in range(N)]

ans = 0

for hand, to in HT:
    current = hands[hand]
    nocurrent = hands[(hand+1)%2]
    print(ring[current:to])
    if nocurrent in ring[current:to]:
        ans += max(kouho(current,to))
    else:
        ans += min(kouho(current,to))
    hands = to
print(ans)