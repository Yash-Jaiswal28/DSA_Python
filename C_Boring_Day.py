t=int(input())
for Z in range(t):
    n,l,r=map(int,input().split())
    v=list(map(int,input().split()))
    # print(v)
    ind1,ind2,ans,sum=0,0,0,0
    while ind1<n and ind2<n:
        while ind2<n and sum<l:
            sum+=v[ind2]
            ind2+=1
        while ind1<ind2  and sum>r:
            sum-=v[ind1]
            ind1+=1
        if sum>=l and sum<=r:
            ans+=1
            ind1=ind2
            sum=0
    print(ans)

