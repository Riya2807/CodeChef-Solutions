try:
    t=int(input())
    for i in range(t):
        A, B, C, D=map(int, input().split())
        if (A+B+C)<=D:
            print('1')
        elif (A+B)<=D:
            print('2')
        else:
            print('3')                
except Exception as e:
    pass