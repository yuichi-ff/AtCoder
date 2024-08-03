N = int(input())
A = list(map(int,input().split()))

AA = sorted(A)

second = AA[-2]

print(A.index(second)+1)

