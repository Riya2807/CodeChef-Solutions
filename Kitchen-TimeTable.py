try:
    N=int(input())
    c=0
    for i in range(N):
        stu_num=int(input())
        scheduled_list=list(map(int,input().split()))
        req_list=list(map(int,input().split()))
        for j in range(len(req_list)):
            if req_list[i]<=scheduled_list[i]:
                c=c+1
            else:
                continue
        print(c)
except Exception as e:
    pass