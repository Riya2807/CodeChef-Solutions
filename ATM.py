'''
a=int(input())
b=int(input())
if a%5==0 and a<b:
    balance=b-(a+0.50)
    print(balance)
elif a>b:
    print(b)
elif a%5!=0:
    print(b)
'''

try:
    x,y = map(float, input().split())
    if x <= y-0.5 and x % 5==0:
        print("%.2f"%(y-x-0.50))
    else:
        print("%.2f"%y)
    
except:
    pass


