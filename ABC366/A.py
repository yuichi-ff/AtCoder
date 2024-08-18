N, T, A = map(int,input().split())

# N 投票者
# T,A 立候補者の開示票数

# 全票数が入れられて勝確かどうか
# → 残りの票数少ない方に加算した時、大きい方より大きいか？

mn = min(T,A)
mx = max(T,A)

ans = "Yes"

if  mn + N-(T+A) > mx:
    ans="No"

print(ans)