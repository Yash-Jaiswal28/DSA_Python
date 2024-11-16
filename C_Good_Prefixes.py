Z= int(input())
for _ in range(Z):
    n=int(input())
    v=list(map(int,input().split()))
    c,mx,sum=0,0,0
    for i in v:
        sum+=i
        mx=max(mx,i)
        if sum-mx==mx:
            c+=1
    print(c)