try:
    t=int(input())
    for t in range(t):
        N, K=map(int,input().split())
        ans=2*(n-k)
        ans+=2*((k-1)/2)
        print(ans)
except Exception as e:
    pass