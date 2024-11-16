Z=int(input())
for _ in range(Z):
    x,y,z,k=map(int,(input().split()))
    ans=0
    for i in range(1,x+1):
        for j in range(1,y+1):
            f=k//(i*j)
            if i*j*f==k and f<=z:
                ans=max(ans,(x-i+1)*(y-j+1)*(z-f+1))

    print(ans)
