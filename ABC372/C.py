N,Q = map(int,input().split())
S = list(input())
XC = [input().split() for _ in range(Q)]

# 整数Xiと文字Ciが与えられる。SのXi番目の文字をCiに置き換え、
# Sに文字列ABCが部分文字列として何箇所含まれるかやう

# N < 2*10^5 (文字列の長さ)
# Q < 2*10^5 (クエリの個数)

# ふつーにやると10^10になってオーバー……
# しかし、クエリの部分は確定でやらないといけないので
# 問題は部分文字列の判定部分？
# 変更されたindexの周辺だけ探索すればそれだけでいいわ
#print(XC)


found = "".join(S).count("ABC")
for j in range(Q):
    
    changeindex = int(XC[j][0])-1

    #なんでおもいつかないんだよおおおおおおおおおおおおおおあああああああ
    #割とこの書き方今後も使うかもしれない。正攻法はAが変更されたら前後がBCか判定、みたいなことをするらしい
    b_S = "".join(S[0 if changeindex <2 else changeindex-2:changeindex+3])
    b_hasABC = "ABC" in b_S
    #print("beforeS:",b_S,b_hasABC)

    S[changeindex] = XC[j][1]

    a_S = "".join(S[0 if changeindex <2 else changeindex-2:changeindex+3])
    
    a_hasABC = "ABC" in a_S
    #print("afterS:",S,a_hasABC)

    if b_hasABC==True and a_hasABC==False:
        found -=1
    elif b_hasABC==False and a_hasABC==True:
        found +=1

    print(found)



    # print(")
