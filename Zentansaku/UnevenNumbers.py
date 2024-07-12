N = int(input())

def digitam(n):
    keta = 0
    while(n > 0):
        n = n//10
        keta+=1
    return keta

print(sum([digitam(a)%2==1 for a in range(1,N+1)]))

# print(sum([a%2==0 for a in range(1,N+1)]))