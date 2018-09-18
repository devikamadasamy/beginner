n=int(input())
for i in range(2,n):
	if n%i==0 and i%2==0:
		print(i,end=" ")
if n%2==0:
	print(n)
