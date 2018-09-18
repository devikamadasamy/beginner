n=int(input())
list1=input().split()
flag=0
for i in range(n-1):
	if n==1:
		break
	if int(list1[i])>int(list1[i+1]):
		flag=1
		break
if flag==0:
	print("yes")
else:
	print("no")
		
