n=int(input())
while(n>=1):
	if n%2==0:
		n=n//2
	else:
		break
if n==1:
	print("yes")
else:
	print("no")
