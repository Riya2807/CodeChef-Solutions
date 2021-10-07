try:
    t=int(input())
    for i in range(t):
        A, B=map(int, input().split())
        if A>0 and B>0:
            print("Solution")
        elif A==0 and B>0:
            print("Liquid")
        elif A>0 and B==0:
            print("Solid")
except Exception as e:
    pass