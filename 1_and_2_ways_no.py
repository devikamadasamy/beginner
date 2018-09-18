n=int(input())
count=0
for i in range(n+1):
	for j in range(n+1):
		k=i+j*2
		if k==n:
			count+=1
print(count)
