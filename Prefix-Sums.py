try:
    t=int(input())
    while(t):
        n=int(input())
        if n%4!=0:
            print("NO")
        else:
            print("YES")
            a=[]
            b=[]
            p=1
            q=n
            flag=0
            check=int(n/2)
            while(check):
                if flag==0:
                    a.append(p)
                    p=p+1
                    flag=1
                else:
                    a.append(q)
                    q=q-1
                    flag=0
                check=check-1
            for i in range(p,q+1):
                b.append(i)
            a.sort()
            b.sort()
            for i in a:
                print(i,end=' ')
            print()
            for i in b:
                print(i,end=' ')
            print()
        t=t-1
except Exception as e:
    pass