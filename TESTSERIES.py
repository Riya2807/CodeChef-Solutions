try:
    t=int(input())
    for i in range(t):
        str1= input()
        c1=str1.count('1')
        c2=str1.count('2')
        if c1==c2 :
            print('DRAW')
        elif c1>c2:
            print('INDIA')
        elif c2>c1:
            print('ENGLAND')
except Exception as e:
    pass
