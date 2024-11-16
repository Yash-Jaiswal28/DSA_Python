Z=int(input())
for _ in range(Z):
    he,n=map(int,input().split())
    v1=list(map(int,input().split()))
    v2=list(map(int,input().split()))
    v=list(zip(v1,v2))
    v.sort(key=lambda x: (-x[0],x[1]))
    l,h=0,1e11
    ans=-1
    while l<=h:
        m=(h+l)//2
        t=he
        for i in range(n):
            t-=(((m+v[i][1]-1)//v[i][1])*v[i][0])
        
        if t<=0:
            h=m-1
            ans=m
        else:
            l=m+1

    print(int(ans))