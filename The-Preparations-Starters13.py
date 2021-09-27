try:
    t=int(input())
    for i in range(t):
        M, N, K=map(int,input().split())
        if (N*K)<M:
            print("YES")
        else:
            print("NO")
except Exception as e:
    pass