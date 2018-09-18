n,m=map(int,input().split())
st=input()
list1=st.split()
flag=0
for i in range(len(list1)):
	if m==int(list1[i]):
		print("yes")
		flag=1
		break
if flag==0:
	print("no")
		
	
