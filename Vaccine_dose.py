#Vaccine dose
try:
    N=int(input())
    for i in range(N):
        D, L, R=map(int,input().split())
        if D>=L and D<=R:
            print("Take second dose now")
        elif D<L:
            print("Too Early")
        elif D>R:
            print("Too Late")
except Exception as e:
    pass