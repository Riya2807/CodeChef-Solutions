try:
    n=int(input())
    for i in range(n):
        num=input()
        l=len(num)
        sum=0
        for j in range(int(l)):
            sum=sum+int(num[j])
        print(sum)
    
except Exception as e:
    pass
