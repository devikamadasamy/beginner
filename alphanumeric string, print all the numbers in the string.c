#include <stdio.h>
#include<string.h>
int main(void) {
	// your code goes here
	char str[20];
	scanf("%s",str);
	int n;
	n=strlen(str);
	int k;
	for(int i=0;i<n;i++){
		k=str[i];
		//printf("%d ",k);
		if(k>=48 && k<=57){
			printf("%c",str[i]);
		}
	}
	return 0;
}
