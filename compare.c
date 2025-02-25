#include <stdio.h>
#include <string.h>
int main()
{
char str1[40],str2[40];
printf("Enter the string:");
scanf("%s",str1);
printf("Enter the string:");
scanf("%s",str2);
if (strcmp(str1,str2)==0)
	{
	printf("The strings are equal");
	}
else 
	{
	printf("Thr strings are not equal");
	}
return 0;
}

