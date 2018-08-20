n=input()
list1=n.split()
string=input()
list2=string.split()
n=int(list1[1])
m=int(list1[0])
if m<n:
	while m>n:
		n=n-m

if(m!=1):
	list2=list2[m-n:]+list2[:m-n]
k=" ".join(list2)
print(k)
