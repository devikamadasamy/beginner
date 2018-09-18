n,k=input().split()
count=0
for i in range(len(n)):
	if int(n[i])==int(k):
		count+=1
print(count)
