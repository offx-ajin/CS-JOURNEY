#include <stdio.h>
int numpalindrome(int num)
{
int remainder,orgnumber,revnumber;
orgnumber=num;
revnumber=0;
while (num!=0)
	{
	remainder=num%10;
	revnumber=revnumber*10+remainder;
	num=num/10;
	}
if (orgnumber==remainder)
	{
	return 1;
	}
else
	{
	return 0;
	}
}
int main()
{
int num,result;
printf ("enter the number");
scanf("%d",&num);
result=numpalindrome(num);
if(result==1)
	{
	printf("%d is a palindrome number ",num);
	}
else 
	{
	printf("%d is not a palindrome num",num);
	}
return 0;
}
