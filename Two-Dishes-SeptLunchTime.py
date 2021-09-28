try:
    t=int(input())
    for i in range(t):
        N, A, B, C=map(int, input().split())
        if B>=N and (A+C)>=N:
                print("YES")
        else:
            print("NO")
except Exception as e:
    pass