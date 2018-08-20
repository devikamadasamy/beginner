# your code goes here
n=input()
list1=n.split()
string=input()
list2=string.split()
n=int(list2[1])
m=int(list2[0])
list2=list2[m-n-1:]+list2[:m-n-1]
k=" ".join(list2)
print(k)
