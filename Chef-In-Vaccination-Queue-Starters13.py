try:
    t=int(input())
    for i in range(t):
        t_count=0
        N, P, X, Y=map(int, input().split())
        v_queue=list(map(int,input().split()))
        for j in range(P):
            if v_queue[j]==0:
                t_count=t_count+X
            elif v_queue[j]==1:
                t_count=t_count+Y
        print(t_count)
except Exception as e:
    pass
