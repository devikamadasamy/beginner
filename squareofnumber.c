
#include<stdio.h>
int main(){
	int num1,sum=0,p;
	scanf("%d",&num1);
	while(num1>0){
		p=num1%10;
		sum=sum+p*p;
		num1=num1/10;}
	printf("%d",sum);
	return 0;
}
