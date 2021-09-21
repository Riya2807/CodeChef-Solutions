#Read the number of test cases.
try:
    T = int(input())
    for i in range(T):
	# Read integers a and b.
       (a, b) = map(int, input().split(' '))
        	
       ans=a+b
       print(ans)
except Exception as e:
    pass