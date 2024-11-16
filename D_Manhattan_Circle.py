Z=int(input())
for _ in range(Z):
    n,m=map(int,(input().split()))
    # print(n,m)
    v=[input() for z in range(n)]

    min_x,max_x,min_y,max_y=m,0,n,0
    for i in range(n):
        for j in range(m):
            if v[i][j]=='#':
                min_x=min(min_x,j)
                max_x=max(max_x,j)
    
    for j in range(m):
        for i in range(n):
            if v[i][j]=='#':
                min_y=min(min_y,i)
                max_y=max(max_y,i)
    
    print(int((max_y+min_y)/2 +1),int((max_x+min_x)/2+1))
    # for i in v:
    #     print(i)