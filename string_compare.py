(n,m,k)=input().split()
k=int(k)
count=0
for i in range(len(n)):
	if n[i]!=m[i]:
		count+=1
if count==k:
	print("yes")
else:
	print("no")
