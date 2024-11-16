t=int(input())
for _ in range(t):
    a,b=map(str,input().split())
    a_swap=b[0]+a[1:]
    b_swap=a[0]+b[1:]
    print(a_swap,b_swap)