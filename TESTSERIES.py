try:
    t=int(input())
    for i in range(t):
        str1= input()
        c2=str1.count('1')
        c3=str1.count('2')
        if c2==c3 :
            print('DRAW')
        elif c2>c3:
            print('INDIA')
        elif c3>c2:
            print('ENGLAND')
except Exception as e:
    pass