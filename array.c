#include <stdio.h>
void sumarray(int arr[],int size);
int main()
{
int size,arr[50];
printf("Enter the size of array");
scanf("%d",&size);
printf("enter the elements");
for (int i=0;i<size;i++)
	{
	scanf("%d",&arr[i]);
	}
sumarray(arr,size);
return 0;
}
void sumarray(int arr[],int size)
{
int sum=0,i;
for (i=0;i<size;i++)
	{
	sum=sum+arr[i];
	}
	printf("The sum is =%d",sum);
	}
