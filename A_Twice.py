Z=int(input())
for _ in range(Z):
    n=int(input())
    v=list(map(int,input().split()))
    mp={}
    for i in v:
        if i not in mp:
            mp[i]=1
        else:
            mp[i]+=1

    ans=0
    for key in mp.values():
        ans+=(key//2)
    print(ans)