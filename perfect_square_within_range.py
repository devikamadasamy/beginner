import math
n,m=map(int,input().split())
count=0
for i in range(n,m+1):
	h=int(math.sqrt(i))
	if h*h==i:
		count+=1
print(count)
	
