#include <stdio.h>
int main()
{
int a[25],i,max=0,min=0,p1=0,p2=0,n;
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
	printf("%d\t\n",a[i]);
	}
max =a[0];
min =a[0];
for (i=1;i<n;i++)
	{
	if(a[i]>max)
		{
		max=a[i];
		p1=i;
		}
	if(a[i]<min)
		{
		min=a[i];
		p2=i;
		}
	}
printf("\nMax is %d in at position %d\n", max,p1);
printf("\nMin is %d in at position %d\n", min,p2);
return 0;
}
