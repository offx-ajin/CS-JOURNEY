#include <stdio.h>
int main()
{
int a[25],i,n,pos=0,key,flag=0;
printf("Enter the array size");
scanf("%d",&n);
printf("Enter the elements :");
for(i=0;i<n;i++)
	{
	scanf("%d",&a[i]);
	}
	printf("the elements are :");
for(i=0;i<n;i++)
	{
	printf("%d\t",a[i]);
	}
printf("\nenter the key:");
scanf("%d",&key);
for(i=0;i<n;i++)
	{
	if(a[i]==key)
		{
		flag=1;
		pos=i;
		break;
		}
		
		
		
	}
	if(flag==1)
		{
		printf("The element is found ");
		printf("the element found %d in position %d",key,pos);
		}
	else
	{
	printf("the element is not found");
	}
		

return 0;
}

