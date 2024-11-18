Z=int(input())
for _ in range(Z):
    n=int(input())
    v=list(map(int,input().split()))
    mp={}
    # print("--------",_)
    for i in v:
        t=n-2
        if t%i==0:
            ck=t//i
            if ck in mp:
                print(ck,i)
                break
            mp[i]=i