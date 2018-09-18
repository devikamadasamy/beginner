string=input()
open=0
close=0
for i in range(len(string)):
	if string[i]=="(":
		open+=1
	else:
		close+=1
if open==close:
	print("yes")
else:
	print("no")
