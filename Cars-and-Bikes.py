try:
    N= int(input())
    for i in range(N):
        Tyre_num=int(input())
        if Tyre_num%4==0:
            print("NO")
        else:
            print("YES")
except Exception as e:
    pass