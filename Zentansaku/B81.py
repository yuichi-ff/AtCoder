N = int(input())

ans = "No"
for i in range(1,9+1):
    for j in range(1,9+1):
        if i*j == N:
            ans = "Yes"
            break

print(ans)