A, B = map(int,input().split())

# print(0 if A+B else 1) #なるほどねえ

ls = [i for i in range(10)]
print(ls[ls.index(A+B)-1]) #A問題でfor系を……まあ解ければいいか……