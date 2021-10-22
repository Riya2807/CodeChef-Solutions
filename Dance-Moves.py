try:
    t=int(input())
    for i in range(t):
        x, y=map(int, input().split())
        if x>y:
            mov=x-y
            print(mov)
        elif x<=y:
            if (y-x)%2==0:
                mov=(y-x)//2
                print(mov)
            else:
                mov=(y-x+1)//2+1
                print(mov)
except Exception as e:
    pass